#!/usr/bin/env python3
"""
Markdown to HTML Converter for LSCode.me

Converts course markdown files to static HTML pages.
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
    SITE_URL, SITE_TITLE, ADMIN_EMAIL, TELEGRAM_BOT,
    OUTPUT_DIR, COURSES_DIR, COURSES, THEME
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


class MarkdownConverter:
    """Converts markdown files to HTML."""
    
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
                'nl2br',
                'sane_lists',
                'attr_list',
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
        # Wrap tables in responsive container
        html = self.wrap_tables(html)
        return html
    
    def wrap_tables(self, html: str) -> str:
        """Wrap tables in a div for responsive horizontal scrolling."""
        return re.sub(
            r'(<table[^>]*>.*?</table>)',
            r'<div class="table-wrapper">\1</div>',
            html,
            flags=re.DOTALL
        )
    
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
        # Skip title and find first paragraph
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
        
        return ' '.join(paragraph)[:200] if paragraph else ""
    
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
            theme=THEME,
            **kwargs
        )
    
    def discover_courses(self) -> list[Course]:
        """Discover all courses and their modules."""
        courses = []
        
        for course_info in COURSES:
            course_path = self.courses_path / course_info['id']
            if not course_path.exists():
                continue
            
            # Read course README
            readme_path = course_path / "README.md"
            description = ""
            if readme_path.exists():
                content = readme_path.read_text(encoding='utf-8')
                description = self.extract_description(content)
            
            # Discover modules
            modules = []
            for item in sorted(course_path.iterdir()):
                if item.is_dir() and item.name[0].isdigit():
                    # Extract module number and name
                    match = re.match(r'^(\d+)_(.+)$', item.name)
                    if match:
                        num = int(match.group(1))
                        name = match.group(2).replace('_', ' ')
                        
                        # Get title from lecture.md
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
                            description=mod_desc[:100],
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
        """Build a lecture page."""
        lecture_path = module.path / "lecture.md"
        if not lecture_path.exists():
            return
        
        content = lecture_path.read_text(encoding='utf-8')
        title = self.extract_title(content)
        html_content = self.convert_markdown(content)
        reading_time = self.calculate_reading_time(content)
        
        # Prepare navigation
        base_url = self.get_base_url(3)  # courses/Course/Module/
        prev_nav = None
        next_nav = None
        
        if prev_module:
            prev_nav = {
                'url': f"{base_url}/courses/{course.id}/{prev_module.id}/",
                'title': prev_module.title
            }
        if next_module:
            next_nav = {
                'url': f"{base_url}/courses/{course.id}/{next_module.id}/",
                'title': next_module.title
            }
        
        html = self.render_template(
            'lecture.html',
            base_url=base_url,
            title=title,
            description=self.extract_description(content),
            content=html_content,
            course_id=course.id,
            course_title=course.title,
            module_title=module.title,
            module_number=module.number,
            reading_time=reading_time,
            prev_module=prev_nav,
            next_module=next_nav,
            quiz_url=f"quiz.html",
            hw_url=f"hw.html",
            links_url=f"links.html",
        )
        
        # Write file
        output_dir = self.output_path / "courses" / course.id / module.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_quiz(self, course: Course, module: Module) -> None:
        """Build a quiz page."""
        quiz_path = module.path / "quiz.md"
        if not quiz_path.exists():
            return
        
        content = quiz_path.read_text(encoding='utf-8')
        quiz_data = self.quiz_parser.parse(content, course.id, module.id)
        
        base_url = self.get_base_url(3)
        
        html = self.render_template(
            'quiz.html',
            base_url=base_url,
            title=quiz_data['title'],
            description=quiz_data.get('description', ''),
            course_id=course.id,
            course_title=course.title,
            module_title=module.title,
            lecture_url=f"index.html",
            question_count=len(quiz_data['questions']),
            time_estimate=len(quiz_data['questions']) * 1,  # 1 min per question
            questions=quiz_data['questions'],
            quiz_data_json=json.dumps(quiz_data),
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "quiz.html").write_text(html, encoding='utf-8')
    
    def build_hw(self, course: Course, module: Module) -> None:
        """Build a homework page."""
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
            title=title,
            description=f"Homework for {module.title}",
            content=f'''
            <article class="lecture-page">
                <nav class="breadcrumb">
                    <a href="{base_url}/">Home</a> &raquo;
                    <a href="{base_url}/courses/">Courses</a> &raquo;
                    <a href="{base_url}/courses/{course.id}/">{course.title}</a> &raquo;
                    <a href="index.html">{module.title}</a> &raquo;
                    <span>Homework</span>
                </nav>
                <div class="lecture-content">{html_content}</div>
                <div class="lecture-nav">
                    <a href="index.html" class="nav-prev">
                        <span class="nav-label">← Back</span>
                        <span class="nav-title">Lecture</span>
                    </a>
                    <a href="quiz.html" class="nav-next">
                        <span class="nav-label">Take Quiz →</span>
                        <span class="nav-title">Quiz</span>
                    </a>
                </div>
            </article>
            ''',
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        (output_dir / "hw.html").write_text(html, encoding='utf-8')
    
    def build_links(self, course: Course, module: Module) -> None:
        """Build a links page."""
        links_path = module.path / "links.md"
        if not links_path.exists():
            return
        
        content = links_path.read_text(encoding='utf-8')
        title = self.extract_title(content)
        html_content = self.convert_markdown(content)
        
        base_url = self.get_base_url(3)
        
        html = self.render_template(
            'base.html',
            base_url=base_url,
            title=title,
            description=f"Additional resources for {module.title}",
            content=f'''
            <article class="lecture-page">
                <nav class="breadcrumb">
                    <a href="{base_url}/">Home</a> &raquo;
                    <a href="{base_url}/courses/">Courses</a> &raquo;
                    <a href="{base_url}/courses/{course.id}/">{course.title}</a> &raquo;
                    <a href="index.html">{module.title}</a> &raquo;
                    <span>Resources</span>
                </nav>
                <div class="lecture-content">{html_content}</div>
            </article>
            ''',
        )
        
        output_dir = self.output_path / "courses" / course.id / module.id
        (output_dir / "links.html").write_text(html, encoding='utf-8')
    
    def build_course_index(self, course: Course) -> None:
        """Build course index page."""
        readme_path = self.courses_path / course.id / "README.md"
        content = ""
        if readme_path.exists():
            content = readme_path.read_text(encoding='utf-8')
        
        html_content = self.convert_markdown(content)
        base_url = self.get_base_url(2)
        
        modules_data = []
        for m in course.modules:
            modules_data.append({
                'number': m.number,
                'title': m.title,
                'description': m.description,
                'url': f"{m.id}/",
                'lecture_url': f"{m.id}/index.html",
                'quiz_url': f"{m.id}/quiz.html",
                'hw_url': f"{m.id}/hw.html",
            })
        
        html = self.render_template(
            'course.html',
            base_url=base_url,
            title=course.title,
            description=course.description,
            course_id=course.id,
            course_title=course.title,
            course_icon=course.icon,
            course_description=course.description,
            module_count=len(course.modules),
            content=html_content,
            modules=modules_data,
        )
        
        output_dir = self.output_path / "courses" / course.id
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_courses_index(self, courses: list[Course]) -> None:
        """Build main courses listing page."""
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
            description="All available courses",
            content=f'''
            <section class="courses-page">
                <h1>📚 All Courses</h1>
                <p>Choose a course to start learning.</p>
                <div class="courses-grid">
                    {''.join(f"""
                    <div class="course-card">
                        <div class="course-icon">{c['icon']}</div>
                        <h3>{c['title']}</h3>
                        <p class="course-modules">{c['modules']} modules</p>
                        <a href="{c['id']}/" class="btn btn-secondary">View Course →</a>
                    </div>
                    """ for c in courses_data)}
                </div>
            </section>
            ''',
        )
        
        output_dir = self.output_path / "courses"
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(html, encoding='utf-8')
    
    def build_home(self, courses: list[Course]) -> None:
        """Build home page - redirect to courses."""
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
    
    def copy_static(self) -> None:
        """Copy static files to output directory."""
        import shutil
        
        static_src = self.base_path / "static"
        static_dst = self.output_path / "static"
        
        if static_dst.exists():
            shutil.rmtree(static_dst)
        
        shutil.copytree(static_src, static_dst)
    
    def build_extra_md_files(self, course: Course) -> None:
        """Build any extra markdown files in course directory (like data/DataSamples.md)."""
        course_path = self.courses_path / course.id
        
        for md_file in course_path.rglob("*.md"):
            # Skip README and module files (already processed)
            rel_path = md_file.relative_to(course_path)
            if md_file.name == "README.md":
                continue
            if rel_path.parts[0][0].isdigit():  # Skip module directories
                continue
            
            content = md_file.read_text(encoding='utf-8')
            title = self.extract_title(content)
            html_content = self.convert_markdown(content)
            
            # Calculate depth for base_url
            depth = len(rel_path.parts) + 1  # courses/Course/path/file
            base_url = self.get_base_url(depth)
            
            html = self.render_template(
                'base.html',
                base_url=base_url,
                title=title,
                description=self.extract_description(content),
                content=f'''
                <article class="lecture-page">
                    <nav class="breadcrumb">
                        <a href="{base_url}/">Home</a> &raquo;
                        <a href="{base_url}/courses/">Courses</a> &raquo;
                        <a href="{base_url}/courses/{course.id}/">{course.title}</a> &raquo;
                        <span>{title}</span>
                    </nav>
                    <div class="lecture-content">{html_content}</div>
                </article>
                ''',
            )
            
            # Output path mirrors source structure
            output_file = self.output_path / "courses" / course.id / rel_path.with_suffix('.html')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(html, encoding='utf-8')
            print(f"    📄 {rel_path}")
    
    def build(self) -> None:
        """Build the entire site."""
        print("🔨 Building LSCode.me site...")
        
        # Discover courses
        courses = self.discover_courses()
        print(f"📚 Found {len(courses)} courses")
        
        # Build each course
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
                self.build_links(course, module)
            
            # Build extra markdown files (like data/DataSamples.md)
            self.build_extra_md_files(course)
        
        # Build index pages
        self.build_courses_index(courses)
        self.build_home(courses)
        
        # Copy static files
        self.copy_static()
        
        print(f"✅ Build complete! Output: {self.output_path}")


def main():
    """Main entry point."""
    base_path = Path(__file__).parent
    converter = MarkdownConverter(base_path)
    converter.build()


if __name__ == "__main__":
    main()
