#!/usr/bin/env python3
"""
Markdown to HTML Converter for LSCode.me Telegram Mini App

Converts course markdown files to static HTML pages optimized for TMA.
"""

import os
import re
import json
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

import markdown
from jinja2 import Environment, FileSystemLoader

from site_metadata import (
    SITE_URL, SITE_TITLE, ADMIN_EMAIL, TELEGRAM_BOT, TELEGRAM_BOT_USERNAME,
    OUTPUT_DIR, COURSES_DIR, COURSES, THEME, TMA_CONFIG
)
from quiz_renderer import QuizParser


@dataclass
class Module:
    """Represents a course module."""
    number: int
    id: str
    title: str
    description: str
    path: Path


@dataclass
class Course:
    """Represents a course."""
    id: str
    title: str
    icon: str
    description: str
    modules: list[Module]


class TMAConverter:
    """Converts markdown files to HTML for Telegram Mini App."""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.output_path = base_path / OUTPUT_DIR
        self.courses_path = base_path / COURSES_DIR
        self.templates_path = base_path / "templates"
        
        # Setup Jinja2
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_path)),
            autoescape=True
        )
        
        # Setup Markdown
        self.md = markdown.Markdown(
            extensions=[
                'fenced_code',
                'codehilite',
                'tables',
                'toc',
                'sane_lists',
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'guess_lang': False,
                }
            }
        )
        
        self.quiz_parser = QuizParser()
    
    def convert_markdown(self, content: str) -> str:
        """Convert markdown to HTML."""
        self.md.reset()
        # Convert .md links to .html
        content = self.convert_links(content)
        html = self.md.convert(content)
        # Add anchors to ordered list items
        html = self.add_list_anchors(html)
        return html
    
    def add_list_anchors(self, html: str) -> str:
        """Add id anchors to ordered list items for linking."""
        counter = [0]  # Use list to allow modification in nested function
        
        def replace_li(match):
            counter[0] += 1
            return f'<li id="item-{counter[0]}">'
        
        # Only add anchors to <li> inside <ol>
        # Process each <ol>...</ol> block separately
        def process_ol(match):
            ol_content = match.group(0)
            counter[0] = 0
            return re.sub(r'<li>', replace_li, ol_content)
        
        return re.sub(r'<ol[^>]*>.*?</ol>', process_ol, html, flags=re.DOTALL)
    
    def convert_links(self, content: str) -> str:
        """Convert .md file links to .html links."""
        # Convert lecture.md to index.html (or just directory)
        content = re.sub(r'\]\(([^)]*/)lecture\.md\)', r'](\1)', content)
        content = re.sub(r'\]\(lecture\.md\)', r'](./)', content)
        # Convert lecture.md#anchor to index.html#anchor
        content = re.sub(r'\]\(([^)]*)lecture\.md(#[^)]+)\)', r'](\1index.html\2)', content)
        # Convert other .md links to .html
        content = re.sub(r'\]\(([^)]+)\.md\)', r'](\1.html)', content)
        content = re.sub(r'\]\(([^)]+)\.md(#[^)]+)\)', r'](\1.html\2)', content)
        return content
    
    def calculate_reading_time(self, content: str) -> int:
        """Calculate estimated reading time in minutes."""
        words = len(content.split())
        return max(1, words // 200)
    
    def extract_title(self, content: str) -> str:
        """Extract title from markdown content."""
        match = re.match(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1) if match else "Untitled"
    
    def extract_description(self, content: str) -> str:
        """Extract first paragraph as description."""
        lines = content.split('\n')
        paragraph = []
        started = False
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                continue
            if stripped.startswith('---'):
                continue
            if stripped:
                started = True
                paragraph.append(stripped)
            elif started and paragraph:
                break
        
        return ' '.join(paragraph)[:150] if paragraph else ""
    
    def get_base_url(self, depth: int = 0) -> str:
        """Get relative base URL based on depth."""
        if depth == 0:
            return "."
        return "/".join([".."] * depth)
    
    def render_template(self, template_name: str, **kwargs) -> str:
        """Render a Jinja2 template."""
        template = self.env.get_template(template_name)
        return template.render(
            site_title=SITE_TITLE,
            site_url=SITE_URL,
            admin_email=ADMIN_EMAIL,
            telegram_bot=TELEGRAM_BOT,
            telegram_bot_username=TELEGRAM_BOT_USERNAME,
            theme=THEME,
            tma_config=TMA_CONFIG,
            **kwargs
        )
    
    def discover_courses(self) -> list[Course]:
        """Discover all courses and their modules."""
        courses = []
        
        for course_info in COURSES:
            course_path = self.courses_path / course_info['id']
            if not course_path.exists():
                continue
            
            readme_path = course_path / "README.md"
            description = ""
            if readme_path.exists():
                content = readme_path.read_text(encoding='utf-8')
                description = self.extract_description(content)
            
            modules = []
            for item in sorted(course_path.iterdir()):
                if item.is_dir() and item.name[0].isdigit():
                    match = re.match(r'^(\d+)_(.+)$', item.name)
                    if match:
                        num = int(match.group(1))
                        name = match.group(2).replace('_', ' ')
                        
                        lecture_path = item / "lecture.md"
                        title = name
                        mod_desc = ""
                        if lecture_path.exists():
                            content = lecture_path.read_text(encoding='utf-8')
                            title = self.extract_title(content)
                            mod_desc = self.extract_description(content)
                        
                        modules.append(Module(
                            number=num,
                            id=item.name,
                            title=title,
                            description=mod_desc[:80],
                            path=item
                        ))
            
            courses.append(Course(
                id=course_info['id'],
                title=course_info['title'],
                icon=course_info['icon'],
                description=description,
                modules=modules
            ))
        
        return courses
    
    def build_lecture(self, course: Course, module: Module, 
                      prev_module: Optional[Module], 
                      next_module: Optional[Module]) -> None:
        """Build a lecture page for TMA."""
        lecture_path = module.path / "lecture.md"
        if not lecture_path.exists():
            return
        
        content = lecture_path.read_text(encoding='utf-8')
        title = self.extract_title(content)
        html_content = self.convert_markdown(content)
        reading_time = self.calculate_reading_time(content)
        
        base_url = self.get_base_url(3)
        prev_nav = None
        next_nav = None
        
        if prev_module:
            prev_nav = {
                'url': f"{base_url}/courses/{course.id}/{prev_module.id}/",
                'title': prev_module.title[:30] + ('...' if len(prev_module.title) > 30 else '')
            }
        if next_module:
            next_nav = {
                'url': f"{base_url}/courses/{course.id}/{next_module.id}/",
                'title': next_module.title[:30] + ('...' if len(next_module.title) > 30 else '')
            }
        
        html = self.render_template(
            'lecture.html',
            base_url=base_url,
            title=title[:40],
            description=self.extract_description(content),
            content=html_content,
            course_id=course.id,
            course_title=course.title,
            module_title=module.title,
            module_number=module.number,
            reading_time=reading_time,
            prev_module=prev_nav,
            next_module=next_nav,
            page_type='lecture',
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_quiz(self, course: Course, module: Module) -> None:
        """Build a quiz page for TMA with Cloud Storage support."""
        quiz_path = module.path / "quiz.md"
        if not quiz_path.exists():
            return
        
        content = quiz_path.read_text(encoding='utf-8')
        quiz_data = self.quiz_parser.parse(content, course.id, module.id)
        
        base_url = self.get_base_url(3)
        
        html = self.render_template(
            'quiz.html',
            base_url=base_url,
            title=f"Quiz: {module.title[:30]}",
            description=quiz_data.get('description', ''),
            course_id=course.id,
            course_title=course.title,
            module_id=module.id,
            module_title=module.title,
            lecture_url=f"index.html",
            question_count=len(quiz_data['questions']),
            time_estimate=len(quiz_data['questions']),
            questions=quiz_data['questions'],
            quiz_data_json=json.dumps(quiz_data),
            page_type='quiz',
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "quiz.html").write_text(html, encoding='utf-8')
    
    def build_hw(self, course: Course, module: Module) -> None:
        """Build a homework page for TMA."""
        hw_path = module.path / "hw.md"
        if not hw_path.exists():
            return
        
        content = hw_path.read_text(encoding='utf-8')
        title = self.extract_title(content)
        html_content = self.convert_markdown(content)
        
        base_url = self.get_base_url(3)
        
        html = self.render_template(
            'base.html',
            base_url=base_url,
            title=f"HW: {title[:30]}",
            description=f"Homework for {module.title}",
            page_type='homework',
            content=f'''
            <article class="lecture-container">
                <div class="lecture-header">
                    <span class="course-badge">{course.title}</span>
                    <div class="module-info">
                        <span class="module-number">Module {module.number} - Homework</span>
                    </div>
                </div>
                <div class="lecture-content">{html_content}</div>
                <div class="lecture-actions">
                    <a href="index.html" class="action-btn">
                        <span class="btn-icon">📖</span>
                        <span class="btn-text">Lecture</span>
                    </a>
                    <a href="quiz.html" class="action-btn primary">
                        <span class="btn-icon">📝</span>
                        <span class="btn-text">Quiz</span>
                    </a>
                </div>
            </article>
            ''',
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        (output_dir / "hw.html").write_text(html, encoding='utf-8')
    
    def build_course_index(self, course: Course) -> None:
        """Build course index page for TMA."""
        base_url = self.get_base_url(2)
        
        modules_data = []
        for m in course.modules:
            modules_data.append({
                'number': m.number,
                'title': m.title,
                'description': m.description,
                'url': f"{m.id}/",
            })
        
        html = self.render_template(
            'course.html',
            base_url=base_url,
            title=course.title[:40],
            description=course.description,
            course_id=course.id,
            course_title=course.title,
            course_icon=course.icon,
            course_description=course.description[:100],
            module_count=len(course.modules),
            modules=modules_data,
            page_type='course',
        )
        
        output_dir = self.output_path / "courses" / course.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_courses_index(self, courses: list[Course]) -> None:
        """Build courses listing page for TMA."""
        base_url = self.get_base_url(1)
        
        courses_data = []
        for c in courses:
            courses_data.append({
                'id': c.id,
                'title': c.title,
                'icon': c.icon,
                'modules': len(c.modules),
            })
        
        html = self.render_template(
            'base.html',
            base_url=base_url,
            title="Courses",
            description="All courses",
            page_type='courses',
            content=f'''
            <section class="tma-home">
                <div class="home-courses">
                    <h2>📚 All Courses</h2>
                    <div class="course-list">
                        {''.join(f"""
                        <a href="{c['id']}/" class="course-item">
                            <span class="course-icon">{c['icon']}</span>
                            <div class="course-info">
                                <h3>{c['title']}</h3>
                                <span class="course-modules">{c['modules']} modules</span>
                            </div>
                            <span class="course-arrow">→</span>
                        </a>
                        """ for c in courses_data)}
                    </div>
                </div>
            </section>
            ''',
        )
        
        output_dir = self.output_path / "courses"
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_home(self, courses: list[Course]) -> None:
        """Build home page for TMA - redirect to courses."""
        html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=courses/">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="courses/">courses</a>...</p>
</body>
</html>'''
        
        self.output_path.mkdir(parents=True, exist_ok=True)
        (self.output_path / "index.html").write_text(html, encoding='utf-8')
    
    def build_progress_page(self) -> None:
        """Build progress tracking page for TMA."""
        html = self.render_template(
            'base.html',
            base_url=".",
            title="Progress",
            description="Your learning progress",
            page_type='progress',
            content='''
            <section class="tma-home">
                <div class="home-hero" style="padding: 16px;">
                    <span class="hero-icon">📊</span>
                    <h1>Your Progress</h1>
                </div>
                <div class="home-progress" id="full-progress">
                    <div class="progress-summary" id="detailed-progress">
                        <p class="loading">Loading progress data...</p>
                    </div>
                </div>
                <div style="padding: 16px;">
                    <button onclick="TMAStorage.clearAll().then(() => location.reload())" 
                            class="action-btn outline" style="width: 100%;">
                        🗑️ Clear All Progress
                    </button>
                </div>
            </section>
            <script>
            document.addEventListener('DOMContentLoaded', async () => {
                const container = document.getElementById('detailed-progress');
                try {
                    const progress = await TMAStorage.getProgress();
                    
                    if (Object.keys(progress).length === 0) {
                        container.innerHTML = `
                            <p class="empty">No progress yet.</p>
                            <p style="text-align:center; margin-top: 8px;">
                                <a href="courses/" class="action-btn primary">Start Learning →</a>
                            </p>
                        `;
                        return;
                    }
                    
                    let html = '<div class="progress-list">';
                    for (const [course, data] of Object.entries(progress)) {
                        const percent = Math.round((data.completed / data.total) * 100);
                        html += `
                            <div class="progress-item">
                                <span class="progress-course">${course}</span>
                                <div class="progress-bar-mini">
                                    <div class="progress-fill-mini" style="width: ${percent}%"></div>
                                </div>
                                <span class="progress-percent">${percent}%</span>
                            </div>
                        `;
                    }
                    html += '</div>';
                    container.innerHTML = html;
                } catch (e) {
                    container.innerHTML = '<p class="error">Could not load progress</p>';
                }
            });
            </script>
            ''',
        )
        
        progress_dir = self.output_path / "progress"
        progress_dir.mkdir(parents=True, exist_ok=True)
        (progress_dir / "index.html").write_text(html, encoding='utf-8')
    
    def copy_static(self) -> None:
        """Copy static files to output directory."""
        import shutil
        
        static_src = self.base_path / "static"
        static_dst = self.output_path / "static"
        
        if static_dst.exists():
            shutil.rmtree(static_dst)
        
        shutil.copytree(static_src, static_dst)
        
        # Also copy highlight.css from build_html if exists
        html_highlight = self.base_path.parent / "build_html" / "static" / "css" / "highlight.css"
        if html_highlight.exists():
            shutil.copy(html_highlight, static_dst / "css" / "highlight.css")
        
        # Copy favicon
        html_favicon = self.base_path.parent / "build_html" / "static" / "favicon.svg"
        if html_favicon.exists():
            shutil.copy(html_favicon, static_dst / "favicon.svg")
    
    def build(self) -> None:
        """Build the entire TMA site."""
        print("🔨 Building LSCode.me Telegram Mini App...")
        
        courses = self.discover_courses()
        print(f"📚 Found {len(courses)} courses")
        
        for course in courses:
            print(f"  📖 Building {course.title}...")
            
            self.build_course_index(course)
            
            for i, module in enumerate(course.modules):
                prev_mod = course.modules[i - 1] if i > 0 else None
                next_mod = course.modules[i + 1] if i < len(course.modules) - 1 else None
                
                print(f"    📄 {module.id}")
                self.build_lecture(course, module, prev_mod, next_mod)
                self.build_quiz(course, module)
                self.build_hw(course, module)
        
        self.build_courses_index(courses)
        self.build_home(courses)
        self.build_progress_page()
        
        self.copy_static()
        
        print(f"✅ TMA build complete! Output: {self.output_path}")


def main():
    """Main entry point."""
    base_path = Path(__file__).parent
    converter = TMAConverter(base_path)
    converter.build()


if __name__ == "__main__":
    main()
