# Build HTML

Tools for building static HTML website from Markdown course files.

## Structure

- `site_metadata.py` - Site configuration (URL, contacts, courses)
- `converter.py` - Main Markdown to HTML converter
- `quiz_renderer.py` - Quiz parser for interactive quizzes
- `build_html.sh` - Build script
- `templates/` - Jinja2 HTML templates
- `static/` - CSS, JS, and assets

## Usage

```bash
./build_html.sh
```

Output will be in `../html/`

## Dependencies

- Python 3.10+
- markdown
- jinja2

Install with:
```bash
pip install markdown jinja2
```
