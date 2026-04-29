#!/usr/bin/env python3
"""
Quiz Parser for LSCode.me Telegram Mini App

Parses quiz markdown files and generates interactive quiz data.
Same as build_html version but can be extended for TMA-specific features.
"""

import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Answer:
    """Represents a quiz answer option."""
    letter: str
    text: str


@dataclass
class Question:
    """Represents a quiz question."""
    number: int
    text: str
    answers: list[Answer] = field(default_factory=list)
    code: Optional[str] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None


class QuizParser:
    """Parses quiz markdown files into structured data."""
    
    def __init__(self):
        self.question_pattern = re.compile(
            r'^##\s+Question\s+(\d+)[:.]?\s*(.+)?$',
            re.MULTILINE
        )
        self.answer_pattern = re.compile(
            r'^([A-D])\)\s+(.+)$',
            re.MULTILINE
        )
        self.answer_key_pattern = re.compile(
            r'\|\s*(\d+)\s*\|\s*([A-D])\s*\|\s*(.+?)\s*\|'
        )
    
    def parse(self, content: str, course_id: str, module_id: str) -> dict:
        """Parse quiz markdown into structured data."""
        # Extract title
        title_match = re.match(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Quiz"
        
        # Extract description
        lines = content.split('\n')
        description = ""
        for line in lines[1:10]:
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('---'):
                description = stripped
                break
        
        # Find answer key
        answer_key = {}
        explanations = {}
        
        answer_key_match = re.search(r'##\s*Answer\s*Key.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if answer_key_match:
            key_section = answer_key_match.group()
            for match in self.answer_key_pattern.finditer(key_section):
                q_num = int(match.group(1))
                answer = match.group(2)
                explanation = match.group(3).strip()
                answer_key[q_num] = answer
                explanations[q_num] = explanation
        
        # Parse questions
        questions = []
        question_splits = re.split(r'(?=##\s+Question\s+\d+)', content)
        
        for split in question_splits:
            q_match = self.question_pattern.match(split.strip())
            if not q_match:
                continue
            
            q_num = int(q_match.group(1))
            q_title = q_match.group(2) or ""
            
            # Get question text
            q_text = ""
            code_block = None
            lines_after_header = split.split('\n')[1:]
            
            in_code = False
            code_lines = []
            text_lines = []
            
            for line in lines_after_header:
                stripped = line.strip()
                
                if stripped.startswith('```'):
                    if in_code:
                        in_code = False
                        code_block = '\n'.join(code_lines)
                        code_lines = []
                    else:
                        in_code = True
                    continue
                
                if in_code:
                    code_lines.append(line)
                    continue
                
                if self.answer_pattern.match(stripped):
                    break
                
                if stripped or text_lines:
                    if stripped and not stripped.startswith('---'):
                        text_lines.append(stripped)
            
            q_text = ' '.join(text_lines).strip()
            if not q_text and q_title:
                q_text = q_title
            
            # Parse answers
            answers = []
            for match in self.answer_pattern.finditer(split):
                answers.append(Answer(
                    letter=match.group(1),
                    text=match.group(2).strip()
                ))
            
            if not answers:
                continue
            
            question = Question(
                number=q_num,
                text=q_text,
                answers=answers,
                code=code_block,
                correct_answer=answer_key.get(q_num),
                explanation=explanations.get(q_num)
            )
            questions.append(question)
        
        questions.sort(key=lambda q: q.number)
        
        return {
            'title': title,
            'description': description,
            'courseId': course_id,
            'moduleId': module_id,
            'questions': [
                {
                    'number': q.number,
                    'text': q.text,
                    'code': q.code,
                    'answers': [{'letter': a.letter, 'text': a.text} for a in q.answers],
                    'correctAnswer': q.correct_answer,
                    'explanation': q.explanation,
                }
                for q in questions
            ]
        }


if __name__ == "__main__":
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: python quiz_renderer.py <quiz.md>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = QuizParser()
    data = parser.parse(content, "test", "test")
    print(json.dumps(data, indent=2, ensure_ascii=False))
