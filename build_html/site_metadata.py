"""
Site metadata configuration for web server build.
"""

# Site Information
SITE_URL = "https://en.lscode.me"
SITE_TITLE = "Python and Linux for Life Science Developers"
SITE_DESCRIPTION = "A comprehensive course designed for life science professionals"

# Contact Information
ADMIN_EMAIL = "admin@lscode.me"
TELEGRAM_BOT = "https://t.me/en_lscode_me_bot"

# Build Configuration
OUTPUT_DIR = "../html"
COURSES_DIR = "../Courses"

# Navigation
COURSES = [
    {
        "id": "DataFundamentals",
        "title": "Data Fundamentals for Life Sciences",
        "icon": "📊",
        "modules": 12,
    },
    {
        "id": "Python",
        "title": "Python for Life Science Developers",
        "icon": "🐍",
        "modules": 11,
    },
    {
        "id": "Linux",
        "title": "Linux for Developers: Unix & Data Pipelines",
        "icon": "🐧",
        "modules": 14,
    },
]

# Theme Configuration
THEME = {
    "primary_color": "#2563eb",
    "secondary_color": "#1e40af",
    "accent_color": "#3b82f6",
    "background_color": "#f8fafc",
    "text_color": "#1e293b",
    "code_background": "#1e293b",
}
