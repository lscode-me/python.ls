"""
Metrics and constants for course quality analysis
"""

from data import get_expected_files, get_expected_module_count, get_all_course_names

# Minimum file sizes (in bytes)
MIN_FILE_SIZES = {
    'lecture.md': 2000,    # Minimum 2KB for lecture
    'hw.md': 800,          # Minimum 800 bytes for homework
    'links.md': 300,       # Minimum 300 bytes for links
    'quiz.md': 500,        # Minimum 500 bytes for quiz
    'README.md': 1000      # Minimum 1KB for README
}

# Recommended file sizes (in bytes)
RECOMMENDED_FILE_SIZES = {
    'lecture.md': 8000,    # Recommended 8KB+ for lecture
    'hw.md': 2000,         # Recommended 2KB+ for homework
    'links.md': 1000,      # Recommended 1KB+ for links
    'quiz.md': 1500,       # Recommended 1.5KB+ for quiz
    'README.md': 3000      # Recommended 3KB+ for README
}

# Module size thresholds
MODULE_SIZE_THRESHOLDS = {
    'small': 5000,         # Small module < 5KB
    'medium': 15000,       # Medium module 5-15KB
    'large': 30000,        # Large module 15-30KB
    'very_large': 50000    # Very large module > 50KB
}

# Keywords for content quality analysis
QUALITY_INDICATORS = {
    'good': [
        '# ', '## ', '### ',  # Good header structure
        '```',                # Code examples
        'example', 'Example', 'exercise', 'Exercise',
        'practice', 'Practice', 'assignment', 'Assignment',
        'task', 'Task', 'activity', 'Activity',
        '**', '*',            # Text emphasis
        '- ', '* ', '1. ',    # Lists
        '| ',                 # Tables
        'https://', 'http://' # Links
    ],
    'concerning': [
        'TODO', 'FIXME', 'XXX', 'HACK',
        'TBD', 'to be done', 'incomplete',
        'placeholder', 'fill in', 'add content',
        'update this', 'needs work'
    ]
}

# Score weights for overall course evaluation
SCORE_WEIGHTS = {
    'structure_completeness': 0.3,  # Structural completeness
    'content_quality': 0.25,        # Content quality
    'file_sizes': 0.2,              # File sizes
    'module_balance': 0.15,         # Module balance
    'readme_quality': 0.1           # README quality
}

# Score thresholds for report color coding
SCORE_THRESHOLDS = {
    'excellent': 0.9,  # Excellent course
    'good': 0.75,      # Good course
    'fair': 0.6,       # Fair course
    'poor': 0.4        # Needs improvement
}

# Validation patterns for README files
README_PATTERNS = {
    'must_have': [
        r'#\s+\w+',          # Course title
        r'##\s+\w+',         # Subheadings
        r'\[\d+_\w+\]',      # Module links
    ],
    'good_to_have': [
        r'📚|📊|🐍|🐧|✅|⚠️|❌',  # Visual emojis
        r'\*\*\w+\*\*',      # Bold text
        r'`\w+`',            # Inline code
        r'\|\s*\w+\s*\|',    # Tables
    ]
}

# Messages for reports
MESSAGES = {
    'excellent': "🟢 Excellent quality",
    'good': "🔵 Good quality",
    'fair': "🟡 Fair quality",
    'poor': "🔴 Needs significant improvement",
    
    'file_missing': "❌ Missing file: {}",
    'file_too_small': "⚠️  File too small: {} ({} bytes)",
    'file_good_size': "✅ Good file size: {} ({} bytes)",
    'unexpected_file': "⚡ Unexpected file: {}",
    
    'module_count_ok': "✅ Module count matches expected: {}",
    'module_count_mismatch': "⚠️  Module count mismatch: {} (expected {})",
    
    'content_quality_good': "✅ Good content quality",
    'content_quality_concerning': "⚠️  Concerning markers found in content",
    
    'balance_good': "✅ Modules are well balanced in size",
    'balance_poor': "⚠️  Modules are uneven in size"
}