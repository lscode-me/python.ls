#!/usr/bin/env python3
"""
Unified Course Quality Management Tool

This script automatically:
1. Standardizes quiz.md files to uniform format (## Question N: Title)
2. Balances correct answer distribution in quiz files
3. Checks language consistency
4. Analyzes course quality and completeness
5. Reports quizzes with too few questions

Usage:
    python check_and_fix_courses.py [options]
    python check_and_fix_courses.py help

Options:
    -v, --verbose    Show detailed report with all information
    --dry-run        Analyze and show what would be changed, but don't modify files
    --courses-dir    Path to courses directory (auto-detected if not specified)

Quiz Format Standard:
    ## Question N: Short Title
    
    Question text here?
    
    A) First option
    B) Second option
    C) Third option
    D) Fourth option
"""

import os
import re
import sys
import glob
import argparse
import random
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from statistics import mean, stdev
from collections import defaultdict, Counter

# Import our metrics and data
from metrics import *
from data import get_expected_files, get_expected_module_count, get_all_course_names, QUIZ_BALANCE_CONFIG

# Minimum questions per quiz
MIN_QUESTIONS = 15


class QuizStandardizer:
    """Standardize quiz format to uniform ## Question N: Title format"""
    
    def __init__(self, courses_dir: str = None):
        self.courses_dir = courses_dir
    
    def detect_format(self, content: str) -> str:
        """Detect quiz format type"""
        has_standard = bool(re.search(r'^## Question \d+:', content, re.MULTILINE))
        has_list = bool(re.search(r'^\d+\.\s+\w+', content, re.MULTILINE))
        has_dash_options = bool(re.search(r'^\s+-\s*[A-D]\)', content, re.MULTILINE))
        
        if has_standard and not has_dash_options:
            return 'STANDARD'
        elif has_list or has_dash_options:
            return 'LIST'
        else:
            return 'UNKNOWN'
    
    def extract_title_from_question(self, question_text: str) -> str:
        """Extract a short title from question text"""
        # Remove code blocks and backticks for title extraction
        clean_text = re.sub(r'`[^`]+`', '', question_text)
        
        # Get first meaningful words
        words = clean_text.split()[:5]
        title = ' '.join(words)
        
        # Clean up
        title = re.sub(r'[^\w\s-]', '', title).strip()
        
        if len(title) > 40:
            title = title[:40] + '...'
        
        return title or 'Question'
    
    def convert_list_to_standard(self, content: str) -> Tuple[str, int]:
        """Convert LIST format quiz to STANDARD format
        
        Input format:
            1. Question text here?
               - A) Option one
               - B) Option two
               - C) Option three
               - D) Option four
        
        Output format:
            ## Question 1: Short Title
            
            Question text here?
            
            A) Option one
            B) Option two
            C) Option three
            D) Option four
        """
        lines = content.split('\n')
        new_lines = []
        converted = 0
        
        i = 0
        in_answer_key = False
        
        while i < len(lines):
            line = lines[i]
            
            # Check for Answer Key section - don't modify it
            if '## Answer Key' in line or '## Answer' in line:
                in_answer_key = True
                new_lines.append(line)
                i += 1
                continue
            
            if in_answer_key:
                new_lines.append(line)
                i += 1
                continue
            
            # Skip ## Questions header
            if line.strip() == '## Questions':
                new_lines.append(line)
                i += 1
                continue
            
            # Match numbered question: "N. Question text"
            q_match = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
            
            if q_match:
                q_num = q_match.group(1)
                q_text = q_match.group(2)
                
                # Extract title from question
                title = self.extract_title_from_question(q_text)
                
                # Add empty line before question if needed
                if new_lines and new_lines[-1].strip():
                    new_lines.append('')
                
                # Write new format header
                new_lines.append(f'## Question {q_num}: {title}')
                new_lines.append('')
                new_lines.append(q_text)
                new_lines.append('')
                
                converted += 1
                i += 1
                
                # Collect all options for this question
                options_found = []
                while i < len(lines):
                    opt_line = lines[i]
                    
                    # Match option format: "   - A) text" or "- A) text"
                    opt_match = re.match(r'^\s*-\s*([A-D])\)\s*(.*)$', opt_line)
                    
                    if opt_match:
                        letter = opt_match.group(1)
                        text = opt_match.group(2)
                        options_found.append(f'{letter}) {text}')
                        i += 1
                    elif opt_line.strip() == '':
                        # Empty line - check if more options follow
                        if i + 1 < len(lines) and re.match(r'^\s*-\s*[A-D]\)', lines[i + 1]):
                            i += 1  # Skip empty line, continue collecting options
                        else:
                            break  # End of question
                    elif re.match(r'^\d+\.', opt_line.strip()):
                        # Next question starts
                        break
                    else:
                        # Unknown line, skip
                        i += 1
                
                # Add collected options
                for opt in options_found:
                    new_lines.append(opt)
                
                new_lines.append('')
            else:
                new_lines.append(line)
                i += 1
        
        return '\n'.join(new_lines), converted
    
    def standardize_file(self, filepath: str, dry_run: bool = False) -> Tuple[bool, str]:
        """Standardize a single quiz file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        format_type = self.detect_format(content)
        
        if format_type == 'STANDARD':
            return False, "Already standard format"
        
        if format_type == 'UNKNOWN':
            return False, "Unknown format - manual review needed"
        
        # Convert LIST to STANDARD
        new_content, converted = self.convert_list_to_standard(content)
        
        if converted == 0:
            return False, "No questions converted"
        
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        
        return True, f"Converted {converted} questions to standard format"
    
    def standardize_all(self, dry_run: bool = False) -> Dict[str, Any]:
        """Standardize all quiz files"""
        if not self.courses_dir:
            return {'error': 'No courses directory'}
        
        courses_path = Path(self.courses_dir)
        quiz_files = list(courses_path.rglob('quiz.md'))
        
        results = {
            'total': len(quiz_files),
            'converted': 0,
            'skipped': 0,
            'failed': 0,
            'details': []
        }
        
        for quiz_file in sorted(quiz_files):
            try:
                relative_path = quiz_file.relative_to(courses_path)
                changed, message = self.standardize_file(str(quiz_file), dry_run=dry_run)
                
                if changed:
                    results['converted'] += 1
                    status = '🔄'
                else:
                    results['skipped'] += 1
                    status = '⏭️'
                
                results['details'].append({
                    'file': str(relative_path),
                    'status': status,
                    'message': message
                })
            except Exception as e:
                results['failed'] += 1
                results['details'].append({
                    'file': str(quiz_file),
                    'status': '❌',
                    'message': str(e)
                })
        
        return results


class QuizBalancer:
    """Balance correct answer distribution in quiz files"""
    
    def __init__(self, courses_dir: str = None):
        self.courses_dir = courses_dir
    
    def has_answer_key(self, quiz_file_path) -> bool:
        """Check if quiz file has an answer key section with table format"""
        try:
            with open(quiz_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '## Answer Key' in content:
                section = content.split('## Answer Key')[1]
                if re.search(r'\|\s*\d+\s*\|\s*[A-D]\s*\|', section):
                    return True
            return False
        except:
            return False
    
    def count_questions(self, quiz_file_path) -> int:
        """Count total number of questions in quiz"""
        try:
            with open(quiz_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return len(re.findall(r'## Question \d+:', content))
        except:
            return 0
    
    def count_answers(self, quiz_file_path) -> int:
        """Count number of answers in answer key"""
        try:
            with open(quiz_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '## Answer Key' not in content:
                return 0
            
            answer_section = content.split('## Answer Key')[1]
            
            lines = answer_section.split('\n')
            section_lines = []
            for line in lines:
                if line.startswith('## '):
                    break
                if line.strip() == '---' and section_lines and not section_lines[-1].strip().startswith('|'):
                    break
                section_lines.append(line)
            
            answer_section = '\n'.join(section_lines)
            matches = re.findall(r'\|\s*\d+\s*\|\s*([A-D])\s*\|', answer_section)
            return len(matches)
        except:
            return 0
    
    def get_answer_distribution(self, quiz_file_path) -> Dict[str, int]:
        """Get distribution of correct answers"""
        try:
            with open(quiz_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            answer_key = self.extract_answer_key(content)
            if not answer_key:
                return {}
            
            distribution = Counter()
            for data in answer_key.values():
                answer = data['answer']
                if answer in ['A', 'B', 'C', 'D']:
                    distribution[answer] += 1
            
            return dict(distribution)
        except:
            return {}
    
    def extract_answer_key(self, content: str) -> Dict[int, Dict]:
        """Extract current answer key from content"""
        answer_key = {}
        table_pattern = r'\| (\d+) \| ([A-D]) \| ([^|]+) \|'
        matches = re.findall(table_pattern, content)
        
        for num, answer, explanation in matches:
            answer_key[int(num)] = {
                'answer': answer,
                'explanation': explanation.strip()
            }
        
        return answer_key
    
    def extract_questions_with_choices(self, content: str) -> Dict[int, Dict]:
        """Extract questions with their answer choices"""
        questions = {}
        
        question_pattern = r'## Question (\d+):(.*?)(?=## Question \d+:|## Answer Key|$)'
        matches = re.findall(question_pattern, content, re.DOTALL)
        
        for num_str, question_content in matches:
            qnum = int(num_str)
            
            choices = {}
            for letter in ['A', 'B', 'C', 'D']:
                choice_pattern = rf'^{letter}\)\s*(.+?)$'
                choice_match = re.search(choice_pattern, question_content, re.MULTILINE)
                if choice_match:
                    choices[letter] = choice_match.group(1).strip()
            
            if len(choices) == 4:
                questions[qnum] = {
                    'content': question_content.strip(),
                    'choices': choices
                }
        
        return questions
    
    def generate_balanced_distribution(self, n: int) -> List[str]:
        """Generate balanced answer distribution for N questions"""
        base_count = n // 4
        remainder = n % 4
        
        distribution = []
        for letter in ['A', 'B', 'C', 'D']:
            distribution.extend([letter] * base_count)
        
        remaining_letters = ['A', 'B', 'C', 'D'][:remainder]
        random.shuffle(remaining_letters)
        distribution.extend(remaining_letters)
        
        random.shuffle(distribution)
        return distribution
    
    def balance_quiz(self, filepath: str, dry_run: bool = False) -> Tuple[bool, str]:
        """Balance answer distribution in a quiz file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        answer_key = self.extract_answer_key(content)
        questions = self.extract_questions_with_choices(content)
        
        if not answer_key:
            return False, "No answer key found"
        
        if not questions:
            return False, "No questions with choices found"
        
        n = len(answer_key)
        
        if set(answer_key.keys()) != set(questions.keys()):
            missing_q = set(answer_key.keys()) - set(questions.keys())
            missing_a = set(questions.keys()) - set(answer_key.keys())
            msg = f"Mismatch: {len(questions)} questions, {len(answer_key)} answers"
            if missing_q:
                msg += f", missing choices: {sorted(missing_q)}"
            return False, msg
        
        target_answers = self.generate_balanced_distribution(n)
        question_numbers = sorted(answer_key.keys())
        new_answer_mapping = dict(zip(question_numbers, target_answers))
        
        new_content = content
        changes_made = 0
        
        for qnum in question_numbers:
            old_answer = answer_key[qnum]['answer']
            new_answer = new_answer_mapping[qnum]
            
            if old_answer == new_answer:
                continue
            
            choices = questions[qnum]['choices']
            correct_text = choices[old_answer]
            
            other_letters = [l for l in ['A', 'B', 'C', 'D'] if l != old_answer]
            target_other_letters = [l for l in ['A', 'B', 'C', 'D'] if l != new_answer]
            
            new_choices = {}
            new_choices[new_answer] = correct_text
            
            for old_letter, new_letter in zip(other_letters, target_other_letters):
                new_choices[new_letter] = choices[old_letter]
            
            q_content = questions[qnum]['content']
            new_q_content = q_content
            
            for letter in ['A', 'B', 'C', 'D']:
                old_choice_pattern = rf'^{letter}\)\s*.+?$'
                old_match = re.search(old_choice_pattern, q_content, re.MULTILINE)
                if old_match:
                    old_line = old_match.group(0)
                    new_line = f"{letter}) {new_choices[letter]}"
                    new_q_content = new_q_content.replace(old_line, new_line, 1)
            
            old_q_block = f"## Question {qnum}:" + q_content
            new_q_block = f"## Question {qnum}:" + new_q_content
            new_content = new_content.replace(old_q_block, new_q_block, 1)
            
            changes_made += 1
        
        # Update answer key
        for qnum in question_numbers:
            old_answer = answer_key[qnum]['answer']
            new_answer = new_answer_mapping[qnum]
            explanation = answer_key[qnum]['explanation']
            
            old_row = f"| {qnum} | {old_answer} | {explanation} |"
            new_row = f"| {qnum} | {new_answer} | {explanation} |"
            new_content = new_content.replace(old_row, new_row, 1)
        
        if changes_made == 0:
            return False, "Already balanced"
        
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        
        new_dist = Counter(target_answers)
        return True, f"Balanced {changes_made} questions -> {dict(new_dist)}"
    
    def balance_all_quizzes(self, dry_run: bool = False) -> Dict[str, Any]:
        """Balance all quiz files"""
        if not self.courses_dir:
            return {'error': 'No courses directory'}
        
        courses_path = Path(self.courses_dir)
        quiz_files = list(courses_path.rglob('quiz.md'))
        
        results = {
            'total': len(quiz_files),
            'balanced': 0,
            'skipped': 0,
            'failed': 0,
            'details': []
        }
        
        for quiz_file in sorted(quiz_files):
            try:
                relative_path = quiz_file.relative_to(courses_path)
                changed, message = self.balance_quiz(str(quiz_file), dry_run=dry_run)
                
                if changed:
                    results['balanced'] += 1
                    status = '✅'
                else:
                    results['skipped'] += 1
                    status = '⏭️'
                
                results['details'].append({
                    'file': str(relative_path),
                    'status': status,
                    'message': message
                })
            except Exception as e:
                results['failed'] += 1
                results['details'].append({
                    'file': str(quiz_file),
                    'status': '❌',
                    'message': str(e)
                })
        
        return results


class CourseAnalyzer:
    """Main class for course analysis"""
    
    def __init__(self, courses_dir: str):
        self.courses_dir = Path(courses_dir)
        self.results = {}
        self.quiz_balancer = QuizBalancer()
        
    def analyze_all_courses(self) -> Dict[str, Any]:
        """Analyzes all courses in the directory"""
        course_dirs = [d for d in self.courses_dir.iterdir() 
                      if d.is_dir() and d.name in get_all_course_names()]
        
        for course_dir in course_dirs:
            self.results[course_dir.name] = self.analyze_course(course_dir)
            
        return self.results
    
    def analyze_course(self, course_dir: Path) -> Dict[str, Any]:
        """Analyzes a single course"""
        course_name = course_dir.name
        result = {
            'course_name': course_name,
            'modules': [],
            'structure_score': 0.0,
            'content_score': 0.0,
            'balance_score': 0.0,
            'readme_score': 0.0,
            'overall_score': 0.0,
            'red_flags': [],
            'stats': {}
        }
        
        readme_path = course_dir / 'README.md'
        if readme_path.exists():
            result['readme_score'] = self.analyze_readme(readme_path)
        else:
            result['red_flags'].append("❌ Missing course README.md")
        
        modules = self.find_modules(course_dir)
        result['stats']['module_count'] = len(modules)
        result['stats']['expected_modules'] = get_expected_module_count(course_name)
        
        if len(modules) != get_expected_module_count(course_name):
            result['red_flags'].append(
                MESSAGES['module_count_mismatch'].format(
                    len(modules), get_expected_module_count(course_name)
                )
            )
        
        module_sizes = []
        for module_dir in modules:
            module_analysis = self.analyze_module(module_dir, course_name)
            result['modules'].append(module_analysis)
            module_sizes.append(module_analysis['total_size'])
        
        result['structure_score'] = self.calculate_structure_score(result['modules'])
        result['content_score'] = self.calculate_content_score(result['modules'])
        result['balance_score'] = self.calculate_balance_score(module_sizes)
        
        result['quiz_score'] = self.calculate_quiz_score(course_dir)
        result['quiz_issues'] = self.get_quiz_issues(course_dir)
        result['quiz_details'] = self.get_quiz_details(course_dir)
        
        result['overall_score'] = (
            result['structure_score'] * SCORE_WEIGHTS['structure_completeness'] +
            result['content_score'] * SCORE_WEIGHTS['content_quality'] +
            result['balance_score'] * SCORE_WEIGHTS['module_balance'] +
            result['readme_score'] * SCORE_WEIGHTS['readme_quality'] +
            result['quiz_score'] * SCORE_WEIGHTS['quiz_quality']
        )
        
        if module_sizes:
            result['stats']['avg_module_size'] = mean(module_sizes)
            result['stats']['min_size'] = min(module_sizes)
            result['stats']['max_size'] = max(module_sizes)
            if len(module_sizes) > 1:
                result['stats']['size_std'] = stdev(module_sizes)
        
        return result
    
    def find_modules(self, course_dir: Path) -> List[Path]:
        """Find all module directories"""
        modules = []
        for item in course_dir.iterdir():
            if item.is_dir() and re.match(r'^\d+_', item.name):
                modules.append(item)
        return sorted(modules)
    
    def analyze_module(self, module_dir: Path, course_name: str) -> Dict[str, Any]:
        """Analyze a single module"""
        expected_files = get_expected_files(course_name)
        result = {
            'name': module_dir.name,
            'path': str(module_dir),
            'files': {},
            'missing_files': [],
            'total_size': 0,
            'structure_complete': True,
            'content_quality': 0.0
        }
        
        for filename in expected_files:
            filepath = module_dir / filename
            if filepath.exists():
                size = filepath.stat().st_size
                result['files'][filename] = {
                    'exists': True,
                    'size': size,
                    'quality': self.assess_file_quality(filepath)
                }
                result['total_size'] += size
            else:
                result['files'][filename] = {'exists': False, 'size': 0, 'quality': 0.0}
                result['missing_files'].append(filename)
                result['structure_complete'] = False
        
        if result['files']:
            qualities = [f['quality'] for f in result['files'].values() if f['exists']]
            result['content_quality'] = mean(qualities) if qualities else 0.0
        
        return result
    
    def assess_file_quality(self, filepath: Path) -> float:
        """Assess the quality of a single file"""
        try:
            content = filepath.read_text(encoding='utf-8')
            size = len(content)
            
            min_size = MIN_FILE_SIZES.get(filepath.name, 500)
            ideal_size = RECOMMENDED_FILE_SIZES.get(filepath.name, 2000)
            
            if size < min_size:
                size_score = 0.3
            elif size < ideal_size:
                size_score = 0.7 + 0.3 * (size - min_size) / (ideal_size - min_size)
            else:
                size_score = 1.0
            
            structure_score = self.analyze_content_structure(content, filepath.suffix)
            return (size_score + structure_score) / 2
        except:
            return 0.0
    
    def analyze_content_structure(self, content: str, file_ext: str) -> float:
        """Analyze content structure quality"""
        if file_ext != '.md':
            return 0.8
        
        score = 0.0
        if re.search(r'^# ', content, re.MULTILINE):
            score += 0.3
        if re.search(r'^## ', content, re.MULTILINE):
            score += 0.3
        if re.search(r'```', content):
            score += 0.2
        if len(content.split('\n\n')) > 3:
            score += 0.2
        
        return min(score, 1.0)
    
    def analyze_readme(self, readme_path: Path) -> float:
        """Analyze README quality"""
        try:
            content = readme_path.read_text(encoding='utf-8')
            score = 0.0
            if len(content) > 200:
                score += 0.4
            if re.search(r'^# ', content):
                score += 0.3
            if 'description' in content.lower():
                score += 0.3
            return min(score, 1.0)
        except:
            return 0.0
    
    def calculate_structure_score(self, modules: List[Dict]) -> float:
        """Calculate overall structure completeness score"""
        if not modules:
            return 0.0
        
        completeness_scores = []
        for module in modules:
            if module['structure_complete']:
                completeness_scores.append(1.0)
            else:
                existing = sum(1 for f in module['files'].values() if f['exists'])
                total = len(module['files'])
                completeness_scores.append(existing / total if total > 0 else 0.0)
        
        return mean(completeness_scores)
    
    def calculate_content_score(self, modules: List[Dict]) -> float:
        """Calculate content quality score"""
        if not modules:
            return 0.0
        return mean([m['content_quality'] for m in modules])
    
    def calculate_balance_score(self, module_sizes: List[int]) -> float:
        """Calculate module balance score"""
        if len(module_sizes) < 2:
            return 1.0
        
        avg_size = mean(module_sizes)
        if avg_size == 0:
            return 0.0
        
        std_dev = stdev(module_sizes)
        cv = std_dev / avg_size
        return min(max(0.0, 1.0 - cv), 1.0)
    
    def calculate_quiz_score(self, course_dir: Path) -> float:
        """Calculate quiz quality score"""
        quiz_files = list(course_dir.rglob('quiz.md'))
        if not quiz_files:
            return 1.0
        
        total_score = 0.0
        critical_failures = 0
        
        for quiz_file in quiz_files:
            try:
                has_answer_key = self.quiz_balancer.has_answer_key(quiz_file)
                if not has_answer_key:
                    critical_failures += 1
                    continue
                
                question_count = self.quiz_balancer.count_questions(quiz_file)
                answer_count = self.quiz_balancer.count_answers(quiz_file)
                
                if question_count == 0:
                    continue
                
                quiz_score = 0.0
                
                if has_answer_key:
                    quiz_score += 0.4
                
                if answer_count == question_count:
                    quiz_score += 0.4
                elif answer_count > 0:
                    ratio = min(answer_count / question_count, 1.0)
                    quiz_score += 0.4 * ratio
                
                # Bonus for having enough questions
                if question_count >= MIN_QUESTIONS:
                    quiz_score += 0.2
                else:
                    quiz_score += 0.2 * (question_count / MIN_QUESTIONS)
                
                total_score += quiz_score
            except:
                critical_failures += 1
        
        if len(quiz_files) == 0:
            return 1.0
        
        failure_penalty = critical_failures / len(quiz_files)
        base_score = total_score / len(quiz_files)
        return min(max(base_score * (1.0 - failure_penalty) ** 2, 0.0), 1.0)
    
    def get_quiz_issues(self, course_dir: Path) -> List[Dict]:
        """Get detailed list of quiz issues"""
        quiz_files = list(course_dir.rglob('quiz.md'))
        issues = []
        
        for quiz_file in quiz_files:
            try:
                relative_path = quiz_file.relative_to(course_dir)
                
                has_answer_key = self.quiz_balancer.has_answer_key(quiz_file)
                if not has_answer_key:
                    issues.append({
                        'file': str(relative_path),
                        'severity': 'CRITICAL',
                        'issue': 'No answer key found',
                        'action': 'Add ## Answer Key section'
                    })
                    continue
                
                question_count = self.quiz_balancer.count_questions(quiz_file)
                answer_count = self.quiz_balancer.count_answers(quiz_file)
                
                if question_count == 0:
                    issues.append({
                        'file': str(relative_path),
                        'severity': 'CRITICAL',
                        'issue': 'No questions in standard format',
                        'action': 'Convert to ## Question N: format'
                    })
                    continue
                
                if answer_count != question_count:
                    issues.append({
                        'file': str(relative_path),
                        'severity': 'CRITICAL',
                        'issue': f'Mismatch: {answer_count} answers for {question_count} questions',
                        'action': f'Fix answer key'
                    })
                
                if question_count < MIN_QUESTIONS:
                    issues.append({
                        'file': str(relative_path),
                        'severity': 'WARNING',
                        'issue': f'Too few questions: {question_count} (min: {MIN_QUESTIONS})',
                        'action': f'Add {MIN_QUESTIONS - question_count} more questions'
                    })
                
            except Exception as e:
                issues.append({
                    'file': str(quiz_file),
                    'severity': 'ERROR',
                    'issue': str(e),
                    'action': 'Check file'
                })
        
        return issues
    
    def get_quiz_details(self, course_dir: Path) -> List[Dict]:
        """Get detailed info about each quiz"""
        quiz_files = list(course_dir.rglob('quiz.md'))
        details = []
        
        for quiz_file in sorted(quiz_files):
            try:
                relative_path = quiz_file.relative_to(course_dir)
                question_count = self.quiz_balancer.count_questions(quiz_file)
                answer_count = self.quiz_balancer.count_answers(quiz_file)
                distribution = self.quiz_balancer.get_answer_distribution(quiz_file)
                
                status = 'OK'
                if question_count == 0:
                    status = 'NO_QUESTIONS'
                elif question_count != answer_count:
                    status = 'MISMATCH'
                elif question_count < MIN_QUESTIONS:
                    status = 'TOO_FEW'
                
                details.append({
                    'file': str(relative_path),
                    'questions': question_count,
                    'answers': answer_count,
                    'balance': dict(distribution) if distribution else None,
                    'status': status
                })
            except:
                details.append({
                    'file': str(quiz_file.name),
                    'questions': 0,
                    'answers': 0,
                    'balance': None,
                    'status': 'ERROR'
                })
        
        return details
    
    def print_report(self, verbose: bool = False):
        """Print report for all courses"""
        if not self.results:
            print("❌ No results")
            return
        
        print("\n" + "="*80)
        print("📊 COURSE ANALYSIS REPORT")
        print("="*80)
        
        total_courses = len(self.results)
        avg_score = mean([r['overall_score'] for r in self.results.values()])
        
        print(f"\n🎯 Statistics:")
        print(f"   Courses: {total_courses}")
        print(f"   Average score: {avg_score:.2f}")
        print(f"   Status: {get_quality_status(avg_score)}")
        
        sorted_courses = sorted(self.results.items(), 
                              key=lambda x: x[1]['overall_score'], reverse=True)
        
        print(f"\n🏆 Ranking:")
        for i, (name, data) in enumerate(sorted_courses, 1):
            score = data['overall_score']
            quiz_score = data.get('quiz_score', 1.0)
            print(f"   {i}. {name}: {score:.2f} {get_quality_status(score)} | Quiz: {quiz_score:.2f}")
        
        # Critical issues
        all_critical = []
        for course_name, data in sorted_courses:
            for issue in data.get('quiz_issues', []):
                if issue['severity'] == 'CRITICAL':
                    all_critical.append({'course': course_name, **issue})
        
        if all_critical:
            print(f"\n🔥 CRITICAL ({len(all_critical)}):")
            for issue in all_critical:
                print(f"   ❌ {issue['course']}/{issue['file']}: {issue['issue']}")
        
        # Warnings (too few questions)
        all_warnings = []
        for course_name, data in sorted_courses:
            for issue in data.get('quiz_issues', []):
                if issue['severity'] == 'WARNING':
                    all_warnings.append({'course': course_name, **issue})
        
        if all_warnings:
            print(f"\n⚠️  WARNINGS ({len(all_warnings)}):")
            for w in all_warnings:
                print(f"   • {w['course']}/{w['file']}: {w['issue']}")
        
        if verbose:
            for course_name, data in sorted_courses:
                self._print_detailed(course_name, data)
    
    def _print_detailed(self, course_name: str, data: Dict):
        """Print detailed report for a course"""
        print(f"\n{'='*60}")
        print(f"📚 {course_name}")
        print(f"{'='*60}")
        
        if 'quiz_details' in data:
            print(f"\n📝 Quizzes:")
            for d in data['quiz_details']:
                icon = '✅' if d['status'] == 'OK' else '⚠️' if d['status'] == 'TOO_FEW' else '❌'
                print(f"   {icon} {d['file']}: {d['questions']}Q/{d['answers']}A")
                if d.get('balance'):
                    print(f"      Distribution: {d['balance']}")


class LanguageChecker:
    """Check language consistency"""
    
    def __init__(self, courses_dir: str):
        self.courses_dir = courses_dir
    
    def check_all(self) -> Dict[str, Any]:
        """Check for Russian text in English courses"""
        english_courses = ['Python', 'Linux']
        quiz_files = []
        
        for course in english_courses:
            pattern = f"{self.courses_dir}/{course}/**/quiz.md"
            quiz_files.extend(glob.glob(pattern, recursive=True))
        
        results = {'total': len(quiz_files), 'issues': 0, 'files': []}
        
        for qf in sorted(quiz_files):
            with open(qf, 'r', encoding='utf-8') as f:
                content = f.read()
            if re.search(r'[а-яё]+', content, re.IGNORECASE):
                results['issues'] += 1
                results['files'].append(qf)
        
        return results


def get_quality_status(score: float) -> str:
    if score >= SCORE_THRESHOLDS['excellent']:
        return "🟢 Excellent"
    elif score >= SCORE_THRESHOLDS['good']:
        return "🔵 Good"
    elif score >= SCORE_THRESHOLDS['fair']:
        return "🟡 Fair"
    else:
        return "🔴 Needs work"


def get_quiz_quality_status(score: float) -> str:
    if score >= 0.9:
        return "✅ Complete"
    elif score >= 0.7:
        return "⚠️ Issues"
    elif score >= 0.4:
        return "❌ Problems"
    else:
        return "💀 Critical"


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Course Quality Tool')
    parser.add_argument('command', nargs='?', default=None, help='"help" for docs')
    parser.add_argument('--courses-dir', default=None)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    
    args = parser.parse_args()
    
    if args.command == 'help':
        print(__doc__)
        return
    
    # Find courses directory
    if args.courses_dir is None:
        script_dir = Path(__file__).parent
        for path in [script_dir / '../Courses', Path.cwd() / 'Courses']:
            if path.exists():
                courses_dir = path.resolve()
                break
        else:
            print("❌ Could not find Courses directory")
            return
    else:
        courses_dir = Path(args.courses_dir).resolve()
    
    print("="*80)
    print("🛠️  COURSE QUALITY MANAGEMENT TOOL")
    print("="*80)
    
    if args.dry_run:
        print("⚠️  DRY RUN MODE\n")
    
    # Step 1: Standardize format
    print("\n📐 Step 1: Standardizing quiz formats...")
    print("-"*60)
    
    standardizer = QuizStandardizer(str(courses_dir))
    std_results = standardizer.standardize_all(dry_run=args.dry_run)
    
    for d in std_results['details']:
        if d['status'] == '🔄':
            print(f"   {d['status']} {d['file']}: {d['message']}")
    
    if std_results['converted'] > 0:
        print(f"\n   Converted: {std_results['converted']} files")
    else:
        print("   ✅ All files already in standard format")
    
    # Step 2: Balance answers
    print("\n⚖️  Step 2: Balancing answer distributions...")
    print("-"*60)
    
    balancer = QuizBalancer(str(courses_dir))
    bal_results = balancer.balance_all_quizzes(dry_run=args.dry_run)
    
    balanced_count = 0
    for d in bal_results['details']:
        if d['status'] == '✅':
            balanced_count += 1
            if args.verbose:
                print(f"   {d['status']} {d['file']}: {d['message']}")
    
    print(f"   Balanced: {balanced_count}, Skipped: {bal_results['skipped']}, Failed: {bal_results['failed']}")
    
    # Step 3: Language check
    print("\n🔤 Step 3: Checking language consistency...")
    print("-"*60)
    
    lang_checker = LanguageChecker(str(courses_dir))
    lang_results = lang_checker.check_all()
    
    if lang_results['issues'] == 0:
        print("   ✅ No Russian text in English courses")
    else:
        print(f"   ⚠️  Russian text in {lang_results['issues']} files")
    
    # Step 4: Analyze
    print("\n📈 Step 4: Analyzing course quality...")
    print("-"*60)
    
    analyzer = CourseAnalyzer(str(courses_dir))
    analyzer.analyze_all_courses()
    analyzer.print_report(verbose=args.verbose)


if __name__ == "__main__":
    main()
