/**
 * LSCode.me - Interactive Quiz Engine
 */

class QuizEngine {
    constructor(quizData) {
        this.data = quizData;
        this.currentQuestion = 0;
        this.answers = {};
        this.submitted = false;
        
        this.init();
    }

    init() {
        this.form = document.getElementById('quiz-form');
        this.prevBtn = document.getElementById('prev-btn');
        this.nextBtn = document.getElementById('next-btn');
        this.submitBtn = document.getElementById('submit-btn');
        this.progressFill = document.getElementById('progress-fill');
        this.progressText = document.getElementById('progress-text');
        this.resultsDiv = document.getElementById('quiz-results');
        
        this.bindEvents();
        this.updateUI();
    }

    bindEvents() {
        // Navigation buttons
        this.prevBtn.addEventListener('click', () => this.navigate(-1));
        this.nextBtn.addEventListener('click', () => this.navigate(1));
        
        // Submit button
        this.submitBtn.addEventListener('click', (e) => {
            e.preventDefault();
            this.submit();
        });

        // Answer selection
        document.querySelectorAll('.answer-option').forEach(option => {
            option.addEventListener('click', (e) => {
                if (this.submitted) return;
                
                const card = option.closest('.question-card');
                const questionNum = parseInt(card.dataset.question);
                const answer = option.dataset.answer;
                
                // Deselect others
                card.querySelectorAll('.answer-option').forEach(opt => {
                    opt.classList.remove('selected');
                });
                
                // Select this one
                option.classList.add('selected');
                option.querySelector('input').checked = true;
                this.answers[questionNum] = answer;
                
                this.updateUI();
            });
        });

        // Review and retake buttons
        document.getElementById('review-btn')?.addEventListener('click', () => this.review());
        document.getElementById('retake-btn')?.addEventListener('click', () => this.retake());
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
        }
    }

    updateUI() {
        const total = this.data.questions.length;
        const current = this.currentQuestion + 1;
        
        // Progress
        const progress = (current / total) * 100;
        this.progressFill.style.width = progress + '%';
        this.progressText.textContent = `Question ${current} of ${total}`;
        
        // Navigation buttons
        this.prevBtn.disabled = this.currentQuestion === 0;
        
        if (this.currentQuestion === total - 1) {
            this.nextBtn.style.display = 'none';
            this.submitBtn.style.display = 'inline-flex';
        } else {
            this.nextBtn.style.display = 'inline-flex';
            this.submitBtn.style.display = 'none';
        }
        
        // Check if all questions answered
        const answeredCount = Object.keys(this.answers).length;
        this.submitBtn.disabled = answeredCount < total;
    }

    submit() {
        if (this.submitted) return;
        
        this.submitted = true;
        this.calculateResults();
    }

    calculateResults() {
        let correct = 0;
        const breakdown = [];
        
        this.data.questions.forEach((question, index) => {
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
                card.querySelectorAll('.answer-option').forEach(option => {
                    const letter = option.dataset.answer;
                    if (letter === question.correctAnswer) {
                        option.classList.add('correct');
                        option.querySelector('.answer-feedback').textContent = '✓ Correct';
                    } else if (letter === userAnswer && !isCorrect) {
                        option.classList.add('incorrect');
                        option.querySelector('.answer-feedback').textContent = '✗ Incorrect';
                    }
                });
            }
        });
        
        this.showResults(correct, this.data.questions.length, breakdown);
    }

    showResults(correct, total, breakdown) {
        const percentage = Math.round((correct / total) * 100);
        
        // Update score display
        document.getElementById('score-value').textContent = correct;
        document.getElementById('score-percentage').textContent = percentage + '%';
        
        // Grade
        let grade = '';
        if (percentage >= 92) grade = '🏆 Excellent!';
        else if (percentage >= 80) grade = '✅ Very Good';
        else if (percentage >= 64) grade = '⚠️ Good';
        else if (percentage >= 48) grade = '📚 Needs Review';
        else grade = '🔄 Study Again';
        
        document.getElementById('score-grade').textContent = grade;
        
        // Breakdown
        const breakdownHtml = breakdown.map(item => `
            <div class="breakdown-item ${item.isCorrect ? 'correct' : 'incorrect'}">
                <span class="q-num">Q${item.number}</span>
                <span class="q-result">${item.isCorrect ? '✓' : '✗'}</span>
                <span class="q-answer">Your: ${item.userAnswer || '-'} | Correct: ${item.correctAnswer}</span>
            </div>
        `).join('');
        
        document.getElementById('results-breakdown').innerHTML = `
            <h4>Answer Breakdown</h4>
            <div class="breakdown-list">${breakdownHtml}</div>
        `;
        
        // Add styles for breakdown
        const style = document.createElement('style');
        style.textContent = `
            .breakdown-list { display: flex; flex-direction: column; gap: 0.5rem; }
            .breakdown-item { display: flex; align-items: center; gap: 1rem; padding: 0.5rem; border-radius: 0.25rem; }
            .breakdown-item.correct { background: #ecfdf5; }
            .breakdown-item.incorrect { background: #fef2f2; }
            .q-num { font-weight: 600; width: 40px; }
            .q-result { font-size: 1.25rem; }
            .q-answer { color: #64748b; font-size: 0.875rem; }
        `;
        document.head.appendChild(style);
        
        // Show results, hide form
        this.form.style.display = 'none';
        this.resultsDiv.style.display = 'block';
        document.querySelector('.quiz-progress').style.display = 'none';
        
        // Save results to localStorage
        this.saveResults(correct, total, percentage);
    }

    saveResults(correct, total, percentage) {
        const key = `quiz_${this.data.courseId}_${this.data.moduleId}`;
        const result = {
            correct,
            total,
            percentage,
            timestamp: new Date().toISOString(),
            answers: this.answers
        };
        
        try {
            const history = JSON.parse(localStorage.getItem('quiz_history') || '{}');
            if (!history[key]) history[key] = [];
            history[key].push(result);
            localStorage.setItem('quiz_history', JSON.stringify(history));
        } catch (e) {
            console.warn('Could not save quiz results to localStorage:', e);
        }
    }

    review() {
        // Show all questions
        document.querySelectorAll('.question-card').forEach(card => {
            card.style.display = 'block';
        });
        
        // Hide results, show form (readonly)
        this.resultsDiv.style.display = 'none';
        this.form.style.display = 'block';
        document.querySelector('.quiz-actions').style.display = 'none';
    }

    retake() {
        // Reset state
        this.currentQuestion = 0;
        this.answers = {};
        this.submitted = false;
        
        // Reset UI
        document.querySelectorAll('.answer-option').forEach(option => {
            option.classList.remove('selected', 'correct', 'incorrect');
            option.querySelector('input').checked = false;
            option.querySelector('.answer-feedback').textContent = '';
        });
        
        document.querySelectorAll('.question-card').forEach((card, index) => {
            card.style.display = index === 0 ? 'block' : 'none';
        });
        
        // Show form, hide results
        this.form.style.display = 'block';
        this.resultsDiv.style.display = 'none';
        document.querySelector('.quiz-progress').style.display = 'block';
        document.querySelector('.quiz-actions').style.display = 'flex';
        
        this.updateUI();
    }
}

// Initialize quiz if data is available
document.addEventListener('DOMContentLoaded', function() {
    if (typeof QUIZ_DATA !== 'undefined') {
        window.quizEngine = new QuizEngine(QUIZ_DATA);
    }
});
