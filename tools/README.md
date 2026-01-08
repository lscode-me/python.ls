# Course Quality Analyzer

A simple toolkit for quickly identifying issues in educational courses.

## 🚀 Quick Start

**Just want to check your courses? Run this:**
```bash
cd tools
python check_courses.py
```

This will analyze all courses and show you exactly what needs attention.

## 📁 Files

- `check_courses.py` - **Simple course checker** (just run this!)
- `course_analyzer.py` - Main analysis engine
- `data.py` - Course structure definitions
- `metrics.py` - Analysis constants and thresholds
- `README.md` - This documentation

## 🎯 What You'll See

The analyzer focuses on **practical issues** that need your attention:

### ❌ Critical Issues
- Missing mandatory files (lecture.md, quiz.md, etc.)
- Wrong number of modules

### ⚠️ Files That Need Work  
- Files that are too small (likely incomplete)
- Missing expected files in modules

### ✅ What's Working Well
- Courses without major issues get a clean report

## 📊 Usage Options

### Quick Check (Recommended)
```bash
python check_courses.py
```

### Advanced Options
```bash
# Summary only (just scores, no details)
python course_analyzer.py --summary

# Check specific course
python course_analyzer.py --course Linux

# Check different folder
python course_analyzer.py --courses-dir /path/to/courses
```

## 🔧 Course Structure Expected

**DataFundamentals (12 modules):** `lecture.md`, `quiz.md`  
**Linux (14 modules):** `lecture.md`, `hw.md`, `links.md`, `quiz.md`  
**Python (11 modules):** `lecture.md`, `hw.md`, `links.md`, `quiz.md`

## ⚙️ Customization

Edit `data.py` to add new courses or change expected files:
```python
COURSE_STRUCTURES['YourCourse'] = {
    'files': ['lecture.md', 'exercise.md'],
    'module_count': 8,
    'description': 'Your Course Description'
}
```

Edit `metrics.py` to adjust file size thresholds and quality indicators.

## 🎯 File Size Guidelines

- **lecture.md**: min 2KB (recommended 8KB+)
- **hw.md**: min 800 bytes (recommended 2KB+)
- **links.md**: min 300 bytes (recommended 1KB+)
- **quiz.md**: min 500 bytes (recommended 1.5KB+)

## 🏆 Quality Scores

- 🟢 **Excellent** (0.9+) - Ready to use
- 🔵 **Good** (0.75+) - Minor tweaks needed  
- 🟡 **Fair** (0.6+) - Some work required
- 🔴 **Needs work** (<0.6) - Significant issues

## 💡 Common Fixes

**"Too small" files** → Add more content, examples, explanations  
**Missing files** → Create the expected files for each module  
**Module count mismatch** → Add missing modules or update expected count in `data.py`

---

*Just run `python check_courses.py` and fix what it tells you! 🚀*