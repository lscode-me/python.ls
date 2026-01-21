# Lecture Quality Guidelines

## Core Principles

Every section in a lecture should be **self-contained** and **clear**. A heading alone is not an explanation. After every heading, there should be text that:
- Explains **what it is** (definition/concept)
- Explains **why it matters** (motivation)
- Shows **how it works** (example)

---

## Section Structure

### ✅ Good Example

```markdown
## 3. Reference Counting (RC)

CPython uses reference counting as its primary garbage collection mechanism.
This means every object maintains a counter tracking how many variables
reference it. When the counter reaches zero, the object is immediately
deallocated from memory.

This approach has advantages:
- Predictable memory deallocation
- Low overhead for most use cases

```python
import sys

x = []
print(sys.getrefcount(x))  # Shows the number of references to the object
```
```

### ❌ Bad Example

```markdown
## 3. Reference Counting (RC)

```python
import sys

x = []
print(sys.getrefcount(x))
```
```

Problems with the bad example:
- No explanation of what Reference Counting is
- No explanation of why you should know this
- Code without context

---

## Section Checklist

- [ ] **Introductory text** — 2-5 sentences explaining the concept
- [ ] **Motivation** — why this is important/useful (can be part of the intro)
- [ ] **Code examples** — with comments explaining what's happening
- [ ] **Practical application** — when/where this is used in real-world scenarios

---

## Style Guidelines

### Text

1. **Start with a definition** — explain what it is in simple terms
2. **Explain the "why"** — motivation matters more than mechanics
3. **Use analogies** — connect new concepts to familiar ones
4. **Avoid unexplained jargon** — if a term is new, define it

### Code

1. **Comment the non-obvious** — not `# create a list`, but `# empty list to accumulate results`
2. **Show the output** — `# Output: [1, 2, 3]`
3. **Use meaningful names** — `user_names` instead of `x`
4. **Minimal examples** — only what's needed to demonstrate the concept

### Structure

1. **Simple to complex** — basic case first, then nuances
2. **One concept per section** — don't mix unrelated topics
3. **Logical transitions** — explain how sections connect to each other

---

## Course-Specific Improvements

### Python Course

- Add **Prerequisites** and **Learning Objectives** sections (like DataFundamentals)
- Every code example should show **expected output**
- Add **"Common Pitfalls"** — what can go wrong
- Add connection to **practical tasks** — where this will be useful

### Linux Course

- Explain **each command** before using it
- Show **real data** — examples with files from `data/`
- Add **step-by-step explanations** for complex pipelines
- Add a **"Common Mistakes"** section

### DataFundamentals Course

- Course is already well-structured, but can be enhanced:
- More **hands-on examples** — things to try yourself
- **Module connections** — how knowledge builds up

---

## Section Improvement Template

When improving a section, use this prompt template:

```
Improve the section "[SECTION NAME]" in the lecture.

Current section:
[PASTE CURRENT TEXT]

Requirements:
1. Add introductory text (2-5 sentences) explaining:
   - What it is
   - Why it matters
   - When it's used
2. Keep all existing code examples
3. Add comments to code explaining what's happening
4. Add expected output for examples
5. Maintain the technical level of the original
6. Don't add fluff — text should be informative
```

---

## Examples of Good Explanations

### Example 1: Explaining a Concept

**Before:**
```markdown
## Mutable vs Immutable

### Immutable example
```python
a = "hello"
b = a
a += "!"
```
```

**After:**
```markdown
## Mutable vs Immutable

Understanding mutability is key to avoiding unexpected bugs in Python.

**Immutable** objects cannot be modified after creation.
When you "change" them, a new object is created, and the old one remains untouched.

**Mutable** objects can be modified "in place".
All references to the object will see the changes.

### Immutable example
```python
a = "hello"
b = a          # b points to the same object as a
a += "!"       # creates a NEW string "hello!", a now points to it
print(a)       # Output: hello!
print(b)       # Output: hello  — b still points to the old object
```
```

### Example 2: Explaining a Command

**Before:**
```markdown
```bash
cat data.csv | cut -d',' -f2 | sort | uniq
```
```

**After:**
```markdown
Let's find all unique values in the second column of a CSV file:

```bash
cat data.csv | cut -d',' -f2 | sort | uniq
#   │           │              │      └── remove duplicates
#   │           │              └── sort (uniq requires sorted input)
#   │           └── extract 2nd column, delimiter is comma
#   └── output file contents

# Example output:
# apple
# banana
# orange
```
```

---

## Improvement Process

1. **Read the entire lecture** — understand the overall structure
2. **Find "bare" sections** — where there's only code without explanation
3. **Add context** — introductory text for each section
4. **Check examples** — are there comments and output?
5. **Connect sections** — add transitions between topics
6. **Proofread** — remove repetition and fluff

---

## Anti-patterns (What to Avoid)

❌ **Code without context** — example without explanation of what it demonstrates

❌ **Orphan heading** — heading immediately followed by code

❌ **Too much theory** — text without examples

❌ **Undefined jargon** — terms that aren't explained

❌ **Examples with `x`, `y`, `foo`, `bar`** — meaningless names

❌ **Long examples** — code that does too much at once
