# Python for Bioinformatics - Quiz

Test your knowledge of bioinformatics concepts and Python applications in computational biology.

---

## Question 1: DNA Basics

Which of the following is NOT a valid DNA nucleotide?

A) Uracil (U)  
B) Adenine (A)  
C) Guanine (G)  
D) Cytosine (C)  

---

## Question 2: Genetic Code

How many nucleotides make up a codon?

A) 2  
B) 4  
C) 6  
D) 3  

---

## Question 3: GC Content

Why is GC content important in molecular biology?

A) It determines the protein size  
B) It affects DNA stability (G-C has 3 hydrogen bonds vs A-T's 2)  
C) It indicates the number of genes  
D) It has no biological significance  

---

## Question 4: FASTA Format

What character starts a sequence identifier in FASTA format?

A) @  
B) #  
C) >  
D) $  

---

## Question 5: Sequence Alignment

What is the purpose of sequence alignment in bioinformatics?

A) To compress sequence data  
B) To find similarities between sequences  
C) To translate DNA to protein  
D) To calculate molecular weight  

---

## Question 6: Python BioPython

Which Python library is most commonly used for bioinformatics tasks?

A) NumPy  
B) Pandas  
C) BioPython  
D) SciPy  

---

## Question 7: DNA Transcription

What is the correct transcription of the DNA sequence "ATGCGA"?

A) UACGCU  
B) TACGCT  
C) AUGCGA  
D) ATGCGA  

---

## Question 8: Reading Frames

How many possible reading frames exist for a single DNA strand?

A) 3  
B) 6  
C) 9  
D) 12  

---

## Question 9: BLAST Algorithm

What does BLAST stand for?

A) Basic Linear Alignment Search Tool  
B) Basic Local Alignment Search Tool  
C) Biological Linear Algorithm Search Tool  
D) Binary Local Alignment Search Tool  

---

## Question 10: Protein Structure

How many levels of protein structure are there?

A) 2  
B) 3  
C) 4  
D) 5  

---

## Question 11: PCR Components

Which of these is NOT required for PCR?

A) DNA template  
B) Primers  
C) DNA polymerase  
D) Restriction enzymes  

---

## Question 12: Phylogenetic Trees

What do branch lengths typically represent in phylogenetic trees?

A) Time since speciation  
B) Geographic distance  
C) Evolutionary distance  
D) Population size  

---

## Question 13: Gene Expression

What technique is commonly used to measure gene expression levels?

A) PCR  
B) RNA-seq  
C) DNA sequencing  
D) Protein crystallography  

---

## Question 14: Bioinformatics Databases

Which database is the primary repository for protein sequences?

A) GenBank  
B) UniProt  
C) EMBL  
D) PDB  

---

## Question 15: Python Data Structures

What Python data structure is best for storing a DNA sequence?

A) List  
B) String  
C) Dictionary  
D) Set  

---

## Question 16: GC Content Calculation

What does this Python code calculate?

```python
def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100
```

A) AT content percentage  
B) GC content percentage  
C) Total nucleotide count  
D) Sequence length  

---

## Question 17: Sequence Manipulation

What would be the output of this code?

```python
seq = "ATGCGATAG"
complement = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
print(complement)
```

A) ATGCGATAG  
B) TACGCTATC  
C) TACGCTAUC  
D) UACGCUAUC  

---

## Question 18: BioPython Usage

In BioPython, which module is used to parse FASTA files?

A) Bio.Seq  
B) Bio.SeqIO  
C) Bio.Align  
D) Bio.BLAST  

---

## Question 19: Real-World Application

Which bioinformatics application would benefit most from parallel processing?

A) Reading a single FASTA file  
B) Genome-wide association studies (GWAS)  
C) Calculating GC content of one sequence  
D) Writing sequence data to a file  

---

## Question 20: Algorithm Complexity

What is the time complexity of the naive string matching algorithm for finding a pattern in a sequence?

A) O(n)  
B) O(n²)  
C) O(nm) where n=text length, m=pattern length  
D) O(log n)  

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Uracil is found in RNA, not DNA |
| 2 | D | A codon consists of 3 consecutive nucleotides |
| 3 | B | GC pairs have 3 hydrogen bonds vs AT's 2, affecting stability |
| 4 | C | FASTA format uses '>' for sequence headers |
| 5 | B | Alignment identifies regions of similarity between sequences |
| 6 | C | BioPython is specifically designed for bioinformatics |
| 7 | C | Transcription: A→U, T→A, G→C, C→G |
| 8 | A | Each DNA strand has 3 possible reading frames |
| 9 | B | BLAST = Basic Local Alignment Search Tool |
| 10 | C | Primary, secondary, tertiary, and quaternary structures |
| 11 | D | PCR doesn't require restriction enzymes |
| 12 | C | Branch lengths represent evolutionary distance |
| 13 | B | RNA-seq is the standard for measuring gene expression |
| 14 | B | UniProt is the main protein sequence database |
| 15 | B | Strings are immutable and perfect for DNA sequences |
| 16 | B | The function calculates GC content percentage |
| 17 | B | Creates DNA complement by base replacement |
| 18 | B | Bio.SeqIO handles sequence input/output operations |
| 19 | B | GWAS analyzes millions of variants across populations |
| 20 | C | Naive string matching has O(nm) complexity |

---

## Scoring Guide

Count your correct answers:

| Result | Grade | Recommendations |
|-----------|--------|--------------|
| **18-20 correct (90-100%)** | 🏆 Excellent! | You have mastered the material excellently. Proceed to the next module. |
| **14-17 correct (70-85%)** | ✅ Good | Good result! Review the topics where you made mistakes. |
| **10-13 correct (50-65%)** | ⚠️ Satisfactory | It is recommended to re-read the corresponding lecture sections. |
| **Less than 10 correct (<50%)** | 📚 Needs Review | Carefully re-read the lecture and try again. |
