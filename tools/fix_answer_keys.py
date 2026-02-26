#!/usr/bin/env python3
"""
Fix answer keys in all quiz.md files.

The QuizBalancer changed the answer key letters without actually rearranging
the answer choices in question bodies. This script reads each quiz, matches
the explanation text to the actual answer choices, and corrects the answer key.
"""

import re
import glob
import sys
from pathlib import Path


def fix_quiz_file(filepath: str, dry_run: bool = False) -> list:
    """Fix answer key in a single quiz file. Returns list of fixes made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '## Answer Key' not in content:
        return []
    
    # Split content into pre-answer-key and answer-key sections
    parts = content.split('## Answer Key', 1)
    before_key = parts[0]
    key_section = '## Answer Key' + parts[1]
    
    # Extract all questions with their choices
    questions = {}
    q_pattern = r'## Question (\d+):.*?(?=## Question \d+:|## Answer Key|\Z)'
    for m in re.finditer(q_pattern, before_key, re.DOTALL):
        q_text = m.group()
        q_num_match = re.match(r'## Question (\d+):', q_text)
        if not q_num_match:
            continue
        qnum = int(q_num_match.group(1))
        
        choices = {}
        for letter in 'ABCD':
            choice_match = re.search(rf'^{letter}\)\s*(.+?)$', q_text, re.MULTILINE)
            if choice_match:
                choices[letter] = choice_match.group(1).strip()
        
        if choices:
            questions[qnum] = choices
    
    # Extract answer key entries and fix them
    fixes = []
    new_key_section = key_section
    
    key_pattern = r'\|\s*(\d+)\s*\|\s*([A-D])\s*\|\s*([^|]+?)\s*\|'
    for m in re.finditer(key_pattern, key_section):
        qnum = int(m.group(1))
        current_letter = m.group(2)
        explanation = m.group(3).strip()
        
        if qnum not in questions:
            continue
        
        choices = questions[qnum]
        
        # Find which choice matches the explanation
        matched_letter = find_matching_choice(explanation, choices)
        
        if matched_letter and matched_letter != current_letter:
            old_row = m.group(0)
            new_row = old_row.replace(f'| {current_letter} |', f'| {matched_letter} |', 1)
            new_key_section = new_key_section.replace(old_row, new_row, 1)
            fixes.append((qnum, current_letter, matched_letter, explanation[:50]))
    
    if fixes and not dry_run:
        new_content = before_key + new_key_section
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return fixes


def find_matching_choice(explanation: str, choices: dict) -> str:
    """Find which choice letter matches the explanation text."""
    expl_clean = explanation.strip().strip('`').strip()
    
    # Strategy 1: Exact match (after stripping backticks)
    for letter, text in choices.items():
        text_clean = text.strip().strip('`').strip()
        if expl_clean == text_clean:
            return letter
    
    # Strategy 2: Explanation contains choice text or vice versa
    for letter, text in choices.items():
        text_clean = text.strip().strip('`').strip()
        if text_clean and (text_clean in expl_clean or expl_clean in text_clean):
            return letter
    
    # Strategy 3: Significant word overlap
    expl_words = set(re.findall(r'\w+', expl_clean.lower()))
    best_letter = None
    best_score = 0
    
    for letter, text in choices.items():
        text_words = set(re.findall(r'\w+', text.lower()))
        if not text_words:
            continue
        # Jaccard-like overlap
        overlap = len(expl_words & text_words)
        score = overlap / max(len(text_words), 1)
        if score > best_score and score > 0.5:
            best_score = score
            best_letter = letter
    
    return best_letter


def main():
    dry_run = '--dry-run' in sys.argv
    courses_dir = 'Courses'
    
    quiz_files = sorted(glob.glob(f'{courses_dir}/**/quiz.md', recursive=True))
    total_fixes = 0
    
    for qf in quiz_files:
        fixes = fix_quiz_file(qf, dry_run=dry_run)
        if fixes:
            print(f"\n{'[DRY RUN] ' if dry_run else ''}Fixed {qf}:")
            for qnum, old, new, expl in fixes:
                print(f"  Q{qnum}: {old} → {new}  ({expl})")
            total_fixes += len(fixes)
    
    action = "Would fix" if dry_run else "Fixed"
    print(f"\n{action} {total_fixes} answer keys in {len(quiz_files)} quiz files.")


if __name__ == '__main__':
    main()
