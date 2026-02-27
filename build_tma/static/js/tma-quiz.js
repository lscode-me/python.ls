/**
 * LSCode TMA - Interactive Quiz Engine with Telegram Cloud Storage
 */

class TMAQuizEngine {
    constructor(quizData, courseId, moduleId) {
        this.data = quizData;
        this.courseId = courseId;
        this.moduleId = moduleId;
        this.currentQuestion = 0;
        this.answers = {};
        this.submitted = false;
        
        this.init();
    }

    init() {
        this.form = document.getElementById('quiz-form');
        this.prevBtn = document.getElementById('btn-prev');
        this.nextBtn = document.getElementById('btn-next');
        this.submitBtn = document.getElementById('btn-submit');
        this.progressFill = document.getElementById('quiz-progress');
        this.progressText = document.getElementById('quiz-progress-text');
        this.resultsDiv = document.getElementById('quiz-results');
        this.cloudStatus = document.getElementById('cloud-status');
        
        this.bindEvents();
        this.updateUI();
        this.loadPreviousResult();
    }

    bindEvents() {
        // Navigation
        this.prevBtn.addEventListener('click', () => {
            hapticFeedback('selection');
            this.navigate(-1);
        });
        
        this.nextBtn.addEventListener('click', () => {
            hapticFeedback('selection');
            this.navigate(1);
        });
        
        this.submitBtn.addEventListener('click', () => {
            hapticFeedback('impact');
            this.submit();
        });

        // Answer selection
        document.querySelectorAll('.answer-item').forEach(item => {
            item.addEventListener('click', () => {
                if (this.submitted) return;
                
                hapticFeedback('selection');
                
                const card = item.closest('.question-card');
                const questionNum = parseInt(card.dataset.question);
                const answer = item.dataset.answer;
                
                // Deselect others
                card.querySelectorAll('.answer-item').forEach(opt => {
                    opt.classList.remove('selected');
                });
                
                // Select this one
                item.classList.add('selected');
                item.querySelector('input').checked = true;
                this.answers[questionNum] = answer;
                
                this.updateUI();
            });
        });

        // Result actions
        document.getElementById('btn-review')?.addEventListener('click', () => {
            hapticFeedback('selection');
            this.review();
        });
        
        document.getElementById('btn-retake')?.addEventListener('click', () => {
            hapticFeedback('impact');
            this.retake();
        });
    }

    async loadPreviousResult() {
        try {
            const previousResult = await TMAStorage.getQuizResult(this.courseId, this.moduleId);
            if (previousResult) {
                // Could show a "Continue where you left off?" prompt
                console.log('Previous result found:', previousResult);
            }
        } catch (e) {
            console.warn('Could not load previous result:', e);
        }
    }

    navigate(direction) {
        const newIndex = this.currentQuestion + direction;
        if (newIndex >= 0 && newIndex < this.data.questions.length) {
            this.showQuestion(this.currentQuestion, false);
            this.currentQuestion = newIndex;
            this.showQuestion(this.currentQuestion, true);
            this.updateUI();
        }
    }

    showQuestion(index, show) {
        const cards = document.querySelectorAll('.question-card');
        if (cards[index]) {
            cards[index].style.display = show ? 'block' : 'none';
            if (show) {
                cards[index].classList.add('fade-in');
            }
        }
    }

    updateUI() {
        const total = this.data.questions.length;
        const current = this.currentQuestion + 1;
        
        // Progress
        const progress = (current / total) * 100;
        this.progressFill.style.width = progress + '%';
        this.progressText.textContent = `${current} / ${total}`;
        
        // Navigation buttons
        this.prevBtn.disabled = this.currentQuestion === 0;
        
        if (this.currentQuestion === total - 1) {
            this.nextBtn.style.display = 'none';
            this.submitBtn.style.display = 'flex';
        } else {
            this.nextBtn.style.display = 'flex';
            this.submitBtn.style.display = 'none';
        }
        
        // Check if all questions answered
        const answeredCount = Object.keys(this.answers).length;
        this.submitBtn.disabled = answeredCount < total;
    }

    async submit() {
        if (this.submitted) return;
        
        this.submitted = true;
        const results = this.calculateResults();
        
        // Save to cloud storage
        await this.saveResults(results);
        
        // Show results
        this.showResults(results);
    }

    calculateResults() {
        let correct = 0;
        const breakdown = [];
        
        this.data.questions.forEach((question) => {
            const userAnswer = this.answers[question.number];
            const isCorrect = userAnswer === question.correctAnswer;
            
            if (isCorrect) correct++;
            
            breakdown.push({
                number: question.number,
                userAnswer,
                correctAnswer: question.correctAnswer,
                isCorrect,
                explanation: question.explanation
            });
            
            // Update UI
            const card = document.querySelector(`[data-question="${question.number}"]`);
            if (card) {
                card.querySelectorAll('.answer-item').forEach(item => {
                    const letter = item.dataset.answer;
                    if (letter === question.correctAnswer) {
                        item.classList.add('correct');
                        item.querySelector('.answer-result').textContent = '✓';
                    } else if (letter === userAnswer && !isCorrect) {
                        item.classList.add('incorrect');
                        item.querySelector('.answer-result').textContent = '✗';
                    }
                });

                // Show explanation if available
                if (question.explanation) {
                    const explanationDiv = document.createElement('div');
                    explanationDiv.className = 'question-explanation';
                    explanationDiv.innerHTML = `<span class="explanation-label">💡 Explanation:</span> ${question.explanation}`;
                    card.appendChild(explanationDiv);
                }
            }
        });
        
        const total = this.data.questions.length;
        const percentage = Math.round((correct / total) * 100);
        
        return { correct, total, percentage, breakdown };
    }

    async saveResults(results) {
        try {
            const saved = await TMAStorage.saveQuizResult(this.courseId, this.moduleId, {
                correct: results.correct,
                total: results.total,
                percentage: results.percentage,
                answers: this.answers,
            });
            
            if (saved) {
                this.cloudStatus.classList.remove('error');
                this.cloudStatus.querySelector('.sync-text').textContent = 'Synced to Telegram Cloud';
                hapticFeedback('success');
            } else {
                throw new Error('Save returned false');
            }
        } catch (e) {
            console.error('Failed to save results:', e);
            this.cloudStatus.classList.add('error');
            this.cloudStatus.querySelector('.sync-text').textContent = 'Saved locally (cloud sync failed)';
            hapticFeedback('warning');
        }
        
        // Also update course progress
        try {
            const courseResults = await TMAStorage.getCourseQuizResults(this.courseId);
            const completedModules = Object.values(courseResults).filter(r => r.percentage >= 80).length;
            const totalModules = 12; // Could make this dynamic
            
            await TMAStorage.saveProgress(this.courseId, {
                completed: completedModules,
                total: totalModules,
            });
        } catch (e) {
            console.warn('Failed to update progress:', e);
        }
    }

    showResults(results) {
        // Update score display
        document.getElementById('score-num').textContent = results.correct;
        document.getElementById('score-percent').textContent = results.percentage + '%';
        
        // Grade badge
        let badge = '';
        if (results.percentage >= 92) badge = '🏆 Excellent!';
        else if (results.percentage >= 80) badge = '✅ Very Good';
        else if (results.percentage >= 64) badge = '⚠️ Good';
        else if (results.percentage >= 48) badge = '📚 Needs Review';
        else badge = '🔄 Study Again';
        
        document.getElementById('score-badge').textContent = badge;
        
        // Summary
        const summaryHtml = `
            <h4>Summary</h4>
            <p>You answered ${results.correct} out of ${results.total} questions correctly.</p>
            ${results.percentage >= 80 
                ? '<p class="success-msg">Great job! You\'ve mastered this module.</p>' 
                : '<p class="retry-msg">Review the lecture and try again to improve your score.</p>'
            }
        `;
        document.getElementById('results-summary').innerHTML = summaryHtml;
        
        // Show results, hide form
        this.form.style.display = 'none';
        document.querySelector('.quiz-progress-container').style.display = 'none';
        this.resultsDiv.style.display = 'block';
        this.resultsDiv.classList.add('fade-in');
    }

    review() {
        // Show all questions
        document.querySelectorAll('.question-card').forEach(card => {
            card.style.display = 'block';
        });
        
        // Hide results, show form
        this.resultsDiv.style.display = 'none';
        this.form.style.display = 'block';
        document.querySelector('.quiz-controls').style.display = 'none';
    }

    retake() {
        // Confirm first
        showConfirm('Start the quiz again?', (confirmed) => {
            if (!confirmed) return;
            
            // Reset state
            this.currentQuestion = 0;
            this.answers = {};
            this.submitted = false;
            
            // Reset UI
            document.querySelectorAll('.answer-item').forEach(item => {
                item.classList.remove('selected', 'correct', 'incorrect');
                item.querySelector('input').checked = false;
                item.querySelector('.answer-result').textContent = '';
            });

            // Remove explanations
            document.querySelectorAll('.question-explanation').forEach(el => el.remove());
            
            document.querySelectorAll('.question-card').forEach((card, index) => {
                card.style.display = index === 0 ? 'block' : 'none';
            });
            
            // Show form, hide results
            this.form.style.display = 'block';
            this.resultsDiv.style.display = 'none';
            document.querySelector('.quiz-progress-container').style.display = 'flex';
            document.querySelector('.quiz-controls').style.display = 'flex';
            
            this.updateUI();
        });
    }
}

// Initialize quiz when data is available
document.addEventListener('DOMContentLoaded', function() {
    if (typeof QUIZ_DATA !== 'undefined' && typeof COURSE_ID !== 'undefined' && typeof MODULE_ID !== 'undefined') {
        window.quizEngine = new TMAQuizEngine(QUIZ_DATA, COURSE_ID, MODULE_ID);
    }
});
