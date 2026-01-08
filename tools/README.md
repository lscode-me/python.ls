# Course Quality Management Tool

A unified toolkit for checking and fixing educational course quality issues.

## 🚀 Quick Start

**Just run this:**
```bash
python check_and_fix_courses.py
```

This will automatically:
1. ✅ Standardize quiz formats
2. ⚖️ Balance answer distributions
3. 🔤 Check language consistency
4. 📊 Analyze course quality

## 📁 Files

- `check_and_fix_courses.py` - **Unified course checker & fixer** (main tool)
- `data.py` - Course structure definitions
- `metrics.py` - Analysis constants and thresholds

## 🎯 What It Does

### Step 1: Quiz Format Standardization
Converts all quiz files to uniform format:
```markdown
## Question 1: Short Title

Question text here?

A) First option
B) Second option
C) Third option
D) Fourth option
```

### Step 2: Answer Distribution Balancing
Ensures ~25% distribution for each answer letter (A, B, C, D) by swapping options.

### Step 3: Language Check
Detects Russian text in English courses (or vice versa).

### Step 4: Quality Analysis
Reports:
- ❌ Critical issues (missing files, wrong module count)
- ⚠️ Warnings (small files, too few questions)
- 📊 Quality scores per course

## 📊 Usage Options

### Standard Run (Recommended)
```bash
python check_and_fix_courses.py
```

### Verbose Mode
```bash
python check_and_fix_courses.py -v
```

### Dry Run (Preview Only)
```bash
python check_and_fix_courses.py --dry-run
```

### Help
```bash
python check_and_fix_courses.py help
```

## 🔧 Course Structure

Course structures are defined in `data.py`. Run the tool to see current configuration:
```bash
python check_and_fix_courses.py help
```

## ⚙️ Customization

Edit `data.py` to add new courses:
```python
COURSE_STRUCTURES['YourCourse'] = {
    'files': ['lecture.md', 'exercise.md'],
    'module_count': 8,
    'description': 'Your Course Description'
}
```

Edit `metrics.py` to adjust thresholds.

## 🎯 File Size Guidelines

| File | Minimum | Recommended |
|------|---------|-------------|
| lecture.md | 2 KB | 8 KB+ |
| hw.md | 800 B | 2 KB+ |
| links.md | 300 B | 1 KB+ |
| quiz.md | 500 B | 1.5 KB+ |

## 📝 Quiz Requirements

- **Minimum 15 questions** per quiz
- **Balanced answers**: ~25% each for A, B, C, D
- **Standard format**: `## Question N: Title`

## 🏆 Quality Scores

| Score | Grade | Status |
|-------|-------|--------|
| 0.9+ | 🟢 Excellent | Ready to use |
| 0.75+ | 🔵 Good | Minor tweaks needed |
| 0.6+ | 🟡 Fair | Some work required |
| <0.6 | 🔴 Needs work | Significant issues |

---

*Just run `python check_and_fix_courses.py` and it handles everything! 🚀*