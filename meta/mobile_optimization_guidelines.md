# Mobile Optimization Guidelines

Recommendations for optimizing course materials for mobile device viewing.

---

## 📱 General Principles

1. **Content width** — aim for ~320-400 characters for ASCII graphics
2. **Vertical orientation** — prefer vertical diagrams over horizontal ones
3. **Minimize horizontal scrolling** — avoid wide tables and diagrams

---

## 🎨 ASCII Diagrams

### ❌ Avoid horizontal layouts

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Creation   │───►│   Storage   │───►│ Processing  │───►│    Usage    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

Problems:
- Requires horizontal scrolling on mobile
- Text becomes too small when scaled
- Hard to read on narrow screens

### ✅ Use vertical layouts

```
┌─────────────┐
│  Creation   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Storage   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Processing  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Usage    │
└─────────────┘
```

Advantages:
- Easy to read on any screen
- No horizontal scrolling required
- Natural top-to-bottom reading order

---

## 📊 Tables

### ❌ Avoid wide tables

```
| Characteristic | Structured        | Semi-structured       | Unstructured          |
|----------------|-------------------|-----------------------|-----------------------|
| Schema         | Strict, external  | Flexible, embedded    | Absent                |
```

### ✅ Split into multiple narrow tables

**Structured data:**
| Characteristic | Value |
|----------------|-------|
| Schema | Strict |
| Examples | SQL, CSV |

**Semi-structured data:**
| Characteristic | Value |
|----------------|-------|
| Schema | Flexible |
| Examples | JSON, XML |

### ✅ Or use lists

**Structured data:**
- Schema: strict, external
- Queries: SQL
- Examples: RDBMS, CSV

---

## 💻 Code Blocks

### Recommended width

- **Maximum:** 60-70 characters per line
- **Optimal:** 40-50 characters per line

### ❌ Lines too long

```bash
samtools view -h aligned.bam | grep "^@" | head -n 20 | awk '{print $1, $2, $3}'
```

### ✅ Split into multiple lines

```bash
samtools view -h aligned.bam \
  | grep "^@" \
  | head -n 20 \
  | awk '{print $1, $2, $3}'
```

---

## 📐 Element Sizes

| Element | Max width | Recommendation |
|---------|-----------|----------------|
| ASCII diagram | 40 characters | Vertical orientation |
| Table | 3-4 columns | Split into parts |
| Code | 60 characters | Line breaks with `\` |
| Text | No limit | Markdown handles it |

---

## 🔧 Verification Tools

### Mobile preview

1. **VS Code Preview** — use a narrow preview window
2. **Chrome DevTools** — mobile device emulation mode
3. **Real device** — test on phone via GitHub

### Automated checking

```bash
# Find lines longer than 70 characters in code blocks
grep -n '.\{71,\}' lecture.md
```

---

## 📝 Pre-publication Checklist

- [ ] ASCII diagrams have vertical orientation
- [ ] Tables are no wider than 4 columns
- [ ] Code lines are no longer than 60-70 characters
- [ ] No horizontally long elements
- [ ] Tested on narrow screen (320px)

---

## 🎯 Optimization Priorities

1. **High:** ASCII diagrams and flow charts
2. **Medium:** Wide data tables
3. **Low:** Long code lines (reader can scroll)

---

## 📚 Examples from Courses

### Data Lifecycle (01_Intro)

Before optimization: horizontal diagram ~75 characters
After optimization: vertical diagram ~15 characters

### Abstraction Levels (01_Intro)

Table with abstraction levels — acceptable, as informativeness is more important.
Can be split into sections if needed.

---

*Last updated: 2026-01-22*
