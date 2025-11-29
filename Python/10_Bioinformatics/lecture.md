# Python for Bioinformatics

## Introduction

Bioinformatics combines biology, computer science, and statistics to analyze biological data. Python has become the de facto language for bioinformatics due to its readability, extensive libraries, and strong community support. This module introduces practical Python applications for common bioinformatics tasks.

---

## 1. Biological Sequences

### 1.1 DNA, RNA, and Protein Sequences

```python
# Basic sequence representation
# DNA (Deoxyribonucleic Acid) - genetic material
# Valid characters: A (Adenine), T (Thymine), G (Guanine), C (Cytosine)
# Sometimes includes: N (any base), R (A or G), Y (C or T), etc. (IUPAC codes)
dna_seq = "ATGCGATCGATCG"

# RNA (Ribonucleic Acid) - messenger molecule
# Valid characters: A (Adenine), U (Uracil), G (Guanine), C (Cytosine)
# Note: U replaces T in RNA
rna_seq = "AUGCGAUCGAUCG"

# Protein (amino acid sequence)
# Valid characters: 20 standard amino acids (single letter codes)
# A=Ala, C=Cys, D=Asp, E=Glu, F=Phe, G=Gly, H=His, I=Ile, K=Lys, L=Leu,
# M=Met, N=Asn, P=Pro, Q=Gln, R=Arg, S=Ser, T=Thr, V=Val, W=Trp, Y=Tyr
# Also: * (stop codon), X (unknown amino acid)
protein_seq = "MRSID"

# Sequence as a class
class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.validate()
    
    def validate(self):
        valid_bases = set('ATCG')
        if not set(self.sequence).issubset(valid_bases):
            raise ValueError("Invalid DNA sequence")
    
    def gc_content(self):
        """
        Calculate GC content percentage
        GC content: ratio of G and C bases (important for DNA stability)
        Higher GC content = stronger binding (3 hydrogen bonds vs 2 for AT)
        """
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return (gc_count / len(self.sequence)) * 100
    
    def complement(self):
        """
        Return complement sequence
        Complement: base pairing rules (A pairs with T, G pairs with C)
        Forms the opposite strand in double helix
        """
        complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complement_dict[base] for base in self.sequence)
    
    def reverse_complement(self):
        """
        Return reverse complement
        Reverse complement: complement sequence read backwards (5' to 3')
        Important for finding genes on opposite DNA strand
        """
        return self.complement()[::-1]
    
    def transcribe(self):
        """
        Transcribe DNA to RNA
        Transcription: process of copying DNA to RNA
        Simply replaces Thymine (T) with Uracil (U)
        """
        return self.sequence.replace('T', 'U')

# Usage
dna = DNASequence("ATGCGATCGATCG")
print(f"GC Content: {dna.gc_content():.2f}%")
print(f"Complement: {dna.complement()}")
print(f"Reverse Complement: {dna.reverse_complement()}")
print(f"RNA: {dna.transcribe()}")
```

### 1.2 Genetic Code and Translation

```python
# Standard genetic code (Universal genetic code)
# Codon: 3 nucleotides that code for one amino acid
# 64 possible codons (4^3) code for 20 amino acids + stop signals
# Genetic code is redundant (multiple codons for same amino acid)
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

def translate(dna_sequence):
    """
    Translate DNA sequence to protein
    Translation: converting nucleotide sequence into amino acid sequence
    Reads sequence in triplets (codons), each coding for one amino acid
    Stops at stop codon (*, TAA, TAG, TGA)
    """
    protein = []
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        amino_acid = CODON_TABLE.get(codon, 'X')  # X = unknown
        if amino_acid == '*':  # Stop codon (translation termination)
            break
        protein.append(amino_acid)
    return ''.join(protein)

# Find all ORFs (Open Reading Frames)
def find_orfs(dna_sequence, min_length=100):
    """
    Find all open reading frames
    ORF: DNA sequence between start codon (ATG) and stop codon
    Potential protein-coding region in genome
    Reading frame: one of three ways to divide sequence into codons
    """
    orfs = []
    start_codon = 'ATG'  # Methionine (Met, M) - translation start signal
    stop_codons = ['TAA', 'TAG', 'TGA']  # Translation termination signals
    
    for frame in range(3):
        for i in range(frame, len(dna_sequence) - 2, 3):
            codon = dna_sequence[i:i+3]
            if codon == start_codon:
                # Found start, look for stop
                for j in range(i + 3, len(dna_sequence) - 2, 3):
                    stop_codon = dna_sequence[j:j+3]
                    if stop_codon in stop_codons:
                        orf = dna_sequence[i:j+3]
                        if len(orf) >= min_length:
                            orfs.append({
                                'sequence': orf,
                                'start': i,
                                'end': j + 3,
                                'frame': frame,
                                'protein': translate(orf)
                            })
                        break
    return orfs

# Usage
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
protein = translate(dna)
print(f"Protein: {protein}")
```

---

## 2. Working with FASTA Files

### 2.1 FASTA Format

FASTA is the most common format for biological sequences.

**FASTA format components:**
- Header line: starts with `>` followed by sequence ID and description
- Sequence lines: actual nucleotide or amino acid sequence
- Can be single-line or multi-line (wrapped at 60-80 characters)
- Multiple sequences separated by new headers

```
>seq1 Description of sequence 1
ATGCGATCGATCGATCGATCG
ATCGATCGATCGATCGATCGA
>seq2 Description of sequence 2
GCTAGCTAGCTAGCTAGCTAG
```

### 2.2 Parsing FASTA Files

```python
from typing import Iterator, Tuple

def parse_fasta(filename: str) -> Iterator[Tuple[str, str, str]]:
    """
    Parse FASTA file yielding (id, description, sequence) tuples
    """
    with open(filename, 'r') as f:
        seq_id = None
        description = None
        sequence = []
        
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                # Yield previous sequence if exists
                if seq_id is not None:
                    yield seq_id, description, ''.join(sequence)
                
                # Parse header
                header = line[1:].split(maxsplit=1)
                seq_id = header[0]
                description = header[1] if len(header) > 1 else ""
                sequence = []
            else:
                sequence.append(line)
        
        # Yield last sequence
        if seq_id is not None:
            yield seq_id, description, ''.join(sequence)

# FASTA writer
def write_fasta(filename: str, sequences: list, line_length=60):
    """
    Write sequences to FASTA file
    sequences: list of (id, description, sequence) tuples
    """
    with open(filename, 'w') as f:
        for seq_id, description, sequence in sequences:
            f.write(f">{seq_id} {description}\n")
            # Write sequence in chunks
            for i in range(0, len(sequence), line_length):
                f.write(sequence[i:i+line_length] + '\n')

# Usage
for seq_id, desc, seq in parse_fasta('sequences.fasta'):
    print(f"ID: {seq_id}")
    print(f"Description: {desc}")
    print(f"Length: {len(seq)}")
    print(f"GC%: {(seq.count('G') + seq.count('C')) / len(seq) * 100:.2f}")
    print()
```

### 2.3 FASTA Statistics

```python
def fasta_statistics(filename: str):
    """Calculate statistics for FASTA file"""
    sequences = list(parse_fasta(filename))
    
    lengths = [len(seq) for _, _, seq in sequences]
    gc_contents = [
        (seq.count('G') + seq.count('C')) / len(seq) * 100
        for _, _, seq in sequences
    ]
    
    stats = {
        'num_sequences': len(sequences),
        'total_length': sum(lengths),
        'min_length': min(lengths),
        'max_length': max(lengths),
        'mean_length': sum(lengths) / len(lengths),
        'mean_gc': sum(gc_contents) / len(gc_contents),
    }
    
    return stats
```

---

## 3. Working with FASTQ Files

### 3.1 FASTQ Format

FASTQ format includes quality scores for each base.

**FASTQ format structure (4 lines per sequence):**
- Line 1: `@` + sequence identifier
- Line 2: raw sequence (DNA/RNA bases)
- Line 3: `+` (optionally followed by same identifier)
- Line 4: quality scores (ASCII characters, one per base)

**Quality scores (Phred scores):**
- Phred score = -10 * log10(error probability)
- Q20 = 99% accuracy, Q30 = 99.9% accuracy
- Higher score = better quality

```
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```

### 3.2 Parsing FASTQ

```python
def parse_fastq(filename: str):
    """Parse FASTQ file"""
    with open(filename, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()
            
            seq_id = header[1:].split()[0]
            yield seq_id, sequence, quality

def quality_to_phred(quality_char: str) -> int:
    """
    Convert quality character to Phred score
    Phred+33 encoding: ASCII value - 33 = quality score
    Example: '!' = 33 - 33 = Q0 (lowest), 'I' = 73 - 33 = Q40 (highest typical)
    """
    return ord(quality_char) - 33

def mean_quality(quality_string: str) -> float:
    """Calculate mean Phred quality score"""
    scores = [quality_to_phred(q) for q in quality_string]
    return sum(scores) / len(scores)

def filter_fastq(input_file: str, output_file: str, 
                 min_quality: float = 20, min_length: int = 50):
    """Filter FASTQ by quality and length"""
    with open(output_file, 'w') as out:
        for seq_id, sequence, quality in parse_fastq(input_file):
            if len(sequence) >= min_length and mean_quality(quality) >= min_quality:
                out.write(f"@{seq_id}\n{sequence}\n+\n{quality}\n")

# Usage
for seq_id, seq, qual in parse_fastq('reads.fastq'):
    avg_qual = mean_quality(qual)
    print(f"{seq_id}: Length={len(seq)}, AvgQual={avg_qual:.1f}")
```

---

## 4. Sequence Alignment

**Sequence Alignment terminology:**
- **Alignment**: arranging sequences to identify regions of similarity
- **Match**: identical nucleotides/amino acids at same position (+score)
- **Mismatch**: different nucleotides/amino acids at same position (-penalty)
- **Gap**: insertion or deletion represented by dash (-) (-penalty)
- **Global alignment**: align entire sequences end-to-end
- **Local alignment**: find best matching subsequences
- **Identity**: percentage of exact matches
- **Similarity**: percentage of matches + conservative substitutions

### 4.1 Simple Alignment Scoring

```python
def simple_alignment_score(seq1: str, seq2: str, 
                          match=1, mismatch=-1, gap=-2) -> int:
    """Score two aligned sequences"""
    score = 0
    for a, b in zip(seq1, seq2):
        if a == '-' or b == '-':
            score += gap
        elif a == b:
            score += match
        else:
            score += mismatch
    return score

# Example
seq1 = "ATCG-AT"
seq2 = "ATCGCAT"
print(f"Alignment score: {simple_alignment_score(seq1, seq2)}")
```

### 4.2 Needleman-Wunsch (Global Alignment)

```python
import numpy as np

def needleman_wunsch(seq1: str, seq2: str, 
                     match=1, mismatch=-1, gap=-2):
    """
    Global sequence alignment using Needleman-Wunsch algorithm
    
    Needleman-Wunsch: dynamic programming algorithm for global alignment
    - Finds optimal alignment of entire sequences
    - Uses scoring matrix to calculate alignment score
    - Traceback to reconstruct actual alignment
    - Time complexity: O(n*m) where n, m are sequence lengths
    """
    n, m = len(seq1), len(seq2)
    
    # Initialize scoring matrix
    score = np.zeros((n + 1, m + 1))
    
    # Initialize first row and column
    for i in range(n + 1):
        score[i][0] = gap * i
    for j in range(m + 1):
        score[0][j] = gap * j
    
    # Fill scoring matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete = score[i-1][j] + gap
            insert = score[i][j-1] + gap
            score[i][j] = max(match_score, delete, insert)
    
    # Traceback
    align1, align2 = '', ''
    i, j = n, m
    
    while i > 0 or j > 0:
        current_score = score[i][j]
        
        if i > 0 and j > 0:
            diagonal = score[i-1][j-1]
            match_mismatch = match if seq1[i-1] == seq2[j-1] else mismatch
            
            if current_score == diagonal + match_mismatch:
                align1 = seq1[i-1] + align1
                align2 = seq2[j-1] + align2
                i -= 1
                j -= 1
                continue
        
        if i > 0 and current_score == score[i-1][j] + gap:
            align1 = seq1[i-1] + align1
            align2 = '-' + align2
            i -= 1
        elif j > 0:
            align1 = '-' + align1
            align2 = seq2[j-1] + align2
            j -= 1
    
    return align1, align2, score[n][m]

# Usage
seq1 = "ATCGAT"
seq2 = "ATCGCAT"
align1, align2, score = needleman_wunsch(seq1, seq2)
print(f"Sequence 1: {align1}")
print(f"Sequence 2: {align2}")
print(f"Score: {score}")
```

---

## 5. Introduction to BioPython

BioPython is the most popular Python library for bioinformatics.

**BioPython key features:**
- Sequence manipulation (Seq, SeqRecord objects)
- File format parsers (FASTA, GenBank, PDB, etc.)
- BLAST and other sequence search tools
- Multiple sequence alignment
- Phylogenetic tree construction
- Access to online biological databases (NCBI, UniProt)
- Protein structure analysis
- Population genetics and more

### 5.1 Installation

```bash
pip install biopython
```

### 5.2 Working with Sequences

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Create a sequence
dna_seq = Seq("ATGCGATCGATCG")

# Transcription and translation
rna_seq = dna_seq.transcribe()
protein_seq = dna_seq.translate()

print(f"DNA: {dna_seq}")
print(f"RNA: {rna_seq}")
print(f"Protein: {protein_seq}")

# Complement and reverse complement
print(f"Complement: {dna_seq.complement()}")
print(f"Reverse complement: {dna_seq.reverse_complement()}")

# GC content
from Bio.SeqUtils import gc_fraction
print(f"GC%: {gc_fraction(dna_seq) * 100:.2f}")
```

### 5.3 Reading/Writing Files with BioPython

```python
from Bio import SeqIO

# Read FASTA file
sequences = list(SeqIO.parse("sequences.fasta", "fasta"))
for record in sequences:
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence: {record.seq[:50]}...")
    print(f"Length: {len(record.seq)}")

# Write FASTA file
records = [
    SeqRecord(Seq("ATGCGATCG"), id="seq1", description="Example sequence 1"),
    SeqRecord(Seq("GCTAGCTAG"), id="seq2", description="Example sequence 2"),
]
SeqIO.write(records, "output.fasta", "fasta")

# Convert between formats
SeqIO.convert("input.fastq", "fastq", "output.fasta", "fasta")
```

### 5.4 Sequence Analysis

```python
from Bio.SeqUtils import molecular_weight, ProtParam

# DNA molecular weight
dna = Seq("ATGCGATCGATCG")
print(f"Molecular weight: {molecular_weight(dna, 'DNA'):.2f}")

# Protein analysis
protein = Seq("MRSID")
analyzed_seq = ProtParam.ProteinAnalysis(str(protein))

print(f"Molecular weight: {analyzed_seq.molecular_weight():.2f}")
print(f"Aromaticity: {analyzed_seq.aromaticity():.3f}")
print(f"Instability index: {analyzed_seq.instability_index():.2f}")
print(f"Isoelectric point: {analyzed_seq.isoelectric_point():.2f}")
```

---

## 6. Pairwise Sequence Alignment with BioPython

```python
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

seq1 = "ATCGAT"
seq2 = "ATCGCAT"

# Global alignment
alignments = pairwise2.align.globalxx(seq1, seq2)
for alignment in alignments[:3]:  # Show top 3
    print(format_alignment(*alignment))

# Local alignment
alignments = pairwise2.align.localxx(seq1, seq2)
for alignment in alignments[:3]:
    print(format_alignment(*alignment))

# Custom scoring
alignments = pairwise2.align.globalms(
    seq1, seq2,
    match=2,      # Match score
    mismatch=-1,  # Mismatch penalty
    open=-2,      # Gap open penalty
    extend=-0.5   # Gap extend penalty
)
```

---

## 7. Working with Biological Databases

**Major biological databases:**
- **NCBI** (National Center for Biotechnology Information): GenBank, PubMed, protein databases
- **UniProt**: protein sequences and functional information
- **Ensembl**: genome annotation and comparative genomics
- **PDB**: protein 3D structures
- **KEGG**: metabolic pathways and diseases

### 7.1 NCBI Entrez

```python
from Bio import Entrez

# Always tell NCBI who you are
Entrez.email = "your.email@example.com"

# Search for sequences
handle = Entrez.esearch(db="nucleotide", term="Homo sapiens[Organism] AND COX1")
record = Entrez.read(handle)
handle.close()

print(f"Total results: {record['Count']}")
print(f"IDs: {record['IdList'][:5]}")

# Fetch sequence
handle = Entrez.efetch(db="nucleotide", id="NM_001354870", rettype="fasta", retmode="text")
fasta_data = handle.read()
handle.close()
print(fasta_data[:200])

# Get GenBank record
handle = Entrez.efetch(db="nucleotide", id="NM_001354870", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print(f"ID: {record.id}")
print(f"Description: {record.description}")
print(f"Features: {len(record.features)}")
```

### 7.2 UniProt

```python
import requests

def fetch_uniprot(uniprot_id):
    """Fetch protein sequence from UniProt"""
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

# Usage
fasta = fetch_uniprot("P04637")  # p53 tumor suppressor
print(fasta[:200])
```

---

## 8. Sequence Motif Finding

```python
import re

def find_motif(sequence: str, motif: str):
    """Find all occurrences of a motif in sequence"""
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            positions.append(i)
    return positions

# With regular expressions
def find_pattern(sequence: str, pattern: str):
    """Find patterns using regex"""
    return [m.start() for m in re.finditer(pattern, sequence)]

# Example: Find restriction sites
def find_restriction_sites(sequence: str):
    """Find common restriction enzyme sites"""
    sites = {
        'EcoRI': 'GAATTC',
        'BamHI': 'GGATCC',
        'PstI': 'CTGCAG',
        'HindIII': 'AAGCTT',
    }
    
    results = {}
    for enzyme, site in sites.items():
        positions = find_motif(sequence, site)
        if positions:
            results[enzyme] = positions
    
    return results

# Usage
dna = "ATGAATTCGGATCCCTGCAGAAGCTT"
sites = find_restriction_sites(dna)
for enzyme, positions in sites.items():
    print(f"{enzyme}: {positions}")
```

---

## 9. Multiple Sequence Alignment

**Multiple Sequence Alignment (MSA):**
- Alignment of 3 or more biological sequences
- Used to find conserved regions across species
- Important for phylogenetic analysis
- Common tools: ClustalW, MUSCLE, MAFFT, T-Coffee
- Applications: identify functional domains, study evolution, design primers

```python
from Bio.Align.Applications import ClustalwCommandline

# Using ClustalW (must be installed)
clustalw_cline = ClustalwCommandline("clustalw2", infile="sequences.fasta")
stdout, stderr = clustalw_cline()

# Read alignment
from Bio import AlignIO
alignment = AlignIO.read("sequences.aln", "clustal")

print(f"Alignment length: {alignment.get_alignment_length()}")
print(f"Number of sequences: {len(alignment)}")

# Calculate consensus
from Bio.Align import AlignInfo
summary = AlignInfo.SummaryInfo(alignment)
consensus = summary.dumb_consensus()
print(f"Consensus: {consensus}")
```

---

## 10. Phylogenetic Trees

**Phylogenetic analysis terminology:**
- **Phylogenetic tree**: diagram showing evolutionary relationships
- **Branch**: line representing evolutionary path
- **Node**: point where branches split (common ancestor)
- **Leaf**: terminal node (present-day species/sequences)
- **UPGMA**: Unweighted Pair Group Method with Arithmetic mean
- **Neighbor-Joining (NJ)**: fast distance-based tree construction
- **Bootstrap**: statistical measure of tree reliability
- **Distance matrix**: pairwise distances between all sequences

```python
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# Calculate distance matrix
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Construct tree
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)

# Draw tree
Phylo.draw_ascii(tree)

# Save tree
Phylo.write(tree, "tree.xml", "phyloxml")
```

---

## 11. Real-World Example: Gene Finder

```python
class GeneFinder:
    """Simple gene finder"""
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.min_protein_length = 100
    
    def find_genes(self):
        """Find all potential genes (ORFs)"""
        genes = []
        
        # Check all 6 reading frames (3 forward, 3 reverse)
        for strand, seq in [(+1, self.sequence), (-1, str(Seq(self.sequence).reverse_complement()))]:
            for frame in range(3):
                orfs = self._find_orfs_in_frame(seq, frame)
                for orf in orfs:
                    orf['strand'] = '+' if strand == 1 else '-'
                    genes.append(orf)
        
        return sorted(genes, key=lambda x: len(x['protein']), reverse=True)
    
    def _find_orfs_in_frame(self, sequence, frame):
        """Find ORFs in a specific reading frame"""
        orfs = []
        start_codon = 'ATG'
        stop_codons = {'TAA', 'TAG', 'TGA'}
        
        i = frame
        while i < len(sequence) - 2:
            codon = sequence[i:i+3]
            
            if codon == start_codon:
                # Found start, look for stop
                start_pos = i
                protein = []
                
                for j in range(i, len(sequence) - 2, 3):
                    codon = sequence[j:j+3]
                    if len(codon) < 3:
                        break
                    
                    aa = CODON_TABLE.get(codon, 'X')
                    
                    if codon in stop_codons:
                        # Found complete ORF
                        if len(protein) >= self.min_protein_length // 3:
                            orfs.append({
                                'start': start_pos,
                                'end': j + 3,
                                'frame': frame,
                                'length': j + 3 - start_pos,
                                'protein': ''.join(protein)
                            })
                        i = j + 3
                        break
                    else:
                        protein.append(aa)
                else:
                    # No stop codon found
                    i += 3
            else:
                i += 3
        
        return orfs

# Usage
sequence = "ATGAAACCCGGGTTTAAATAGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGTAG"
finder = GeneFinder(sequence)
genes = finder.find_genes()

for i, gene in enumerate(genes, 1):
    print(f"Gene {i}:")
    print(f"  Position: {gene['start']}-{gene['end']}")
    print(f"  Strand: {gene['strand']}")
    print(f"  Frame: {gene['frame']}")
    print(f"  Length: {gene['length']} bp")
    print(f"  Protein: {gene['protein'][:50]}...")
    print()
```

---

## 12. Best Practices for Bioinformatics

### 12.1 Data Validation

```python
def validate_dna(sequence: str) -> bool:
    """Validate DNA sequence"""
    return all(base in 'ATCGN' for base in sequence.upper())

def validate_protein(sequence: str) -> bool:
    """Validate protein sequence"""
    valid_aa = set('ACDEFGHIKLMNPQRSTVWY*')
    return all(aa in valid_aa for aa in sequence.upper())

def sanitize_sequence(sequence: str) -> str:
    """Remove whitespace and numbers from sequence"""
    return ''.join(c for c in sequence if c.isalpha())
```

### 12.2 Memory-Efficient Processing

```python
def process_large_fasta(filename: str):
    """Process large FASTA files efficiently"""
    for seq_id, description, sequence in parse_fasta(filename):
        # Process one sequence at a time
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence)
        
        # Don't store all sequences in memory
        print(f"{seq_id}: {len(sequence)} bp, GC={gc_content:.2%}")
```

### 12.3 Error Handling

```python
def safe_translate(sequence: str) -> str:
    """Translate with error handling"""
    try:
        if not validate_dna(sequence):
            raise ValueError("Invalid DNA sequence")
        
        if len(sequence) % 3 != 0:
            print(f"Warning: Sequence length ({len(sequence)}) not divisible by 3")
        
        return translate(sequence)
    
    except Exception as e:
        print(f"Translation error: {e}")
        return None
```

---

## Summary

In this module, you learned:

1. **Biological Sequences** - Representation and manipulation of DNA, RNA, and proteins
2. **File Formats** - Working with FASTA and FASTQ files
3. **Sequence Alignment** - Global and local alignment algorithms
4. **BioPython** - Using the most popular bioinformatics library
5. **Databases** - Accessing NCBI and UniProt programmatically
6. **Motif Finding** - Searching for patterns in sequences
7. **Gene Finding** - Identifying open reading frames
8. **Best Practices** - Writing robust bioinformatics code

### Next Steps

- Explore more BioPython modules (Blast, Phylo, PDB)
- Learn about genomic data formats (SAM/BAM, VCF, GFF)
- Study machine learning for bioinformatics
- Practice with real datasets from public databases
- Contribute to open-source bioinformatics projects

### Additional Resources

- BioPython Tutorial: http://biopython.org/DIST/docs/tutorial/Tutorial.html
- Rosalind Problems: http://rosalind.info/
- NCBI E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
