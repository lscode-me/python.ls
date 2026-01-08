"""
Course structure definitions and expected data
"""

# Quiz balance configuration
QUIZ_BALANCE_CONFIG = {
    'max_deviation_percent': 7.0,  # Maximum allowed deviation from 25% per answer choice
    'max_shuffle_attempts': 100,   # Maximum attempts to achieve balance
    'target_distribution': 25.0    # Target percentage for each answer choice (A, B, C, D)
}

# Expected files for each course type
COURSE_STRUCTURES = {
    'DataFundamentals': {
        'files': ['lecture.md', 'hw.md', 'links.md', 'quiz.md'],
        'module_count': 12,
        'description': 'Data Fundamentals for Life Sciences'
    },
    'Linux': {
        'files': ['lecture.md', 'hw.md', 'links.md', 'quiz.md'],
        'module_count': 14,
        'description': 'Unix & Data Pipelines'
    },
    'Python': {
        'files': ['lecture.md', 'hw.md', 'links.md', 'quiz.md'],
        'module_count': 11,
        'description': 'Python for Life Science Developers'
    }
}

# Course catalog with detailed information
COURSE_CATALOG = {
    'DataFundamentals': {
        'full_name': 'Data Fundamentals for Life Sciences',
        'description': 'Essential data concepts, encodings, file formats, and data processing fundamentals',
        'modules': [
            '01_Intro',
            '02_NumberSystems', 
            '03_Encodings',
            '04_FileFormats',
            '05_JSON',
            '06_YAML',
            '07_Markup',
            '08_ConfigFiles',
            '09_TabularData',
            '10_Compression',
            '11_Checksums',
            '12_DataTransfer'
        ],
        'target_audience': ['Bioinformaticians', 'Life Science Researchers', 'Healthcare Data Engineers']
    },
    'Linux': {
        'full_name': 'Unix & Data Pipelines',
        'description': 'Unix tools, shell scripting, and CLI-based data processing',
        'modules': [
            '01_Unix_Streams',
            '02_Files_Inodes_Descriptors',
            '03_Shell_Programming',
            '04_Coreutils',
            '05_Grep_Sed_Awk',
            '06_Structured_Data',
            '07_Streaming_Analytics',
            '08_Log_Processing',
            '09_Performance_Parallelism',
            '10_Streams_IPC',
            '11_Bash_Glue',
            '12_Python_Pipelines',
            '13_Complex_Pipelines',
            '14_Final_Project'
        ],
        'target_audience': ['Engineers', 'Data Scientists', 'System Administrators']
    },
    'Python': {
        'full_name': 'Python for Life Science Developers',
        'description': 'Python fundamentals, OOP, functional programming, and bioinformatics applications',
        'modules': [
            '01_Objects',
            '02_Functions',
            '03_Files',
            '04_Testing',
            '05_Iteration',
            '06_Streams',
            '07_Coroutines',
            '08_OOP',
            '09_Pythonic',
            '10_Protocols',
            '11_Bioinformatics'
        ],
        'target_audience': ['Life Science Developers', 'Bioinformaticians', 'Research Scientists']
    }
}

# Helper functions
def get_expected_files(course_name: str) -> list:
    """Get expected files for a course"""
    return COURSE_STRUCTURES.get(course_name, {}).get('files', [])

def get_expected_module_count(course_name: str) -> int:
    """Get expected module count for a course"""
    return COURSE_STRUCTURES.get(course_name, {}).get('module_count', 0)

def get_course_description(course_name: str) -> str:
    """Get course description"""
    return COURSE_CATALOG.get(course_name, {}).get('description', '')

def get_all_course_names() -> list:
    """Get list of all course names"""
    return list(COURSE_STRUCTURES.keys())

def is_valid_course(course_name: str) -> bool:
    """Check if course name is valid"""
    return course_name in COURSE_STRUCTURES
