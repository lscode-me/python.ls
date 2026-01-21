# Build TMA (Telegram Mini App)

Tools for building static HTML website optimized for Telegram Mini App from Markdown course files.

## Structure

- `site_metadata.py` - Site configuration with TMA-specific settings
- `converter.py` - Main Markdown to HTML converter for TMA
- `quiz_renderer.py` - Quiz parser for interactive quizzes
- `build_tma.sh` - Build script
- `templates/` - Jinja2 HTML templates (mobile-optimized)
- `static/` - CSS, JS with Telegram WebApp SDK integration

## Features

- **Telegram WebApp SDK** - Full integration with Telegram Mini App platform
- **Cloud Storage** - Quiz results saved to Telegram Cloud Storage (key-value)
- **Adaptive Theme** - Automatically adapts to user's Telegram theme
- **Mobile First** - Optimized for mobile viewing
- **Progress Tracking** - Track learning progress across sessions

## Usage

```bash
./build_tma.sh
```

Output will be in `../html/tma/`

## Telegram Cloud Storage Keys

Quiz results are stored with keys in format:
- `lscode_quiz_{course}_{module}` - Individual quiz results
- `lscode_progress_{course}` - Course progress
- `lscode_user_preferences` - User settings

## Dependencies

- Python 3.10+
- markdown
- jinja2

Install with:
```bash
pip install markdown jinja2
```

## Setting up Telegram Bot

1. Create a bot via @BotFather
2. Enable Mini App for your bot
3. Set the Mini App URL to `https://en.lscode.me/tma/`
