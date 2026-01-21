"""
Site metadata configuration for Telegram Mini App build.
"""

# Site Information
SITE_URL = "https://en.lscode.me"
SITE_TITLE = "LSCode - Python & Linux for Life Sciences"
SITE_DESCRIPTION = "Interactive learning platform for life science developers"

# Contact Information  
ADMIN_EMAIL = "admin@lscode.me"
TELEGRAM_BOT = "https://t.me/en_lscode_me_bot"
TELEGRAM_BOT_USERNAME = "en_lscode_me_bot"

# Build Configuration
OUTPUT_DIR = "../html/tma"
COURSES_DIR = "../Courses"

# Telegram Mini App Configuration
TMA_CONFIG = {
    # Enable Telegram WebApp SDK
    "enable_webapp_sdk": True,
    
    # Cloud Storage keys prefix
    "storage_prefix": "lscode_",
    
    # Quiz result storage key pattern: {prefix}quiz_{course}_{module}
    "quiz_key_pattern": "quiz_{course}_{module}",
    
    # Progress tracking key pattern: {prefix}progress_{course}
    "progress_key_pattern": "progress_{course}",
    
    # User preferences key
    "preferences_key": "user_preferences",
    
    # Max items to store in cloud (Telegram limit)
    "max_cloud_items": 1024,
    
    # Theme settings (auto-detect from Telegram)
    "auto_theme": True,
}

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

# Theme Configuration (Telegram will override with user's theme)
THEME = {
    "primary_color": "#2563eb",
    "secondary_color": "#1e40af",
    "accent_color": "#3b82f6",
    # These will be replaced by Telegram theme colors
    "background_color": "var(--tg-theme-bg-color, #f8fafc)",
    "text_color": "var(--tg-theme-text-color, #1e293b)",
    "hint_color": "var(--tg-theme-hint-color, #64748b)",
    "link_color": "var(--tg-theme-link-color, #2563eb)",
    "button_color": "var(--tg-theme-button-color, #2563eb)",
    "button_text_color": "var(--tg-theme-button-text-color, #ffffff)",
}
