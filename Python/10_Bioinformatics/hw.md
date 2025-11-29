# Bioinformatics - Homework


## Assignment 1: DNA Sequence Analysis

Create a comprehensive DNA sequence analyzer that:
- Validates DNA sequences
- Calculates GC content
- Finds complement and reverse complement
- Transcribes to RNA
- Identifies potential start and stop codons
- Calculates melting temperature (Tm)

Your goal:
Master basic DNA sequence operations and understand fundamental molecular biology concepts in code.

Test with:
- Normal sequences
- Sequences with ambiguous bases (N)
- Very long sequences (performance testing)


## Assignment 2: Genetic Code Implementation

Implement a complete genetic code translation system:
- Create the standard genetic code table
- Implement translation (DNA/RNA to protein)
- Handle all three reading frames
- Identify ORFs (Open Reading Frames)
- Support alternative genetic codes (mitochondrial, bacterial)
- Handle frame shifts and incomplete codons

Your goal:
Understand the genetic code and translation process deeply through implementation.

Requirements:
- Support both DNA and RNA input
- Handle sequences that don't start with ATG
- Report all possible ORFs with their positions


## Assignment 3: FASTA File Parser

Build a robust FASTA file parser and writer:
- Parse multi-sequence FASTA files
- Handle wrapped sequences (multi-line)
- Calculate statistics (length, GC%, N50)
- Filter sequences by criteria (length, GC content)
- Convert between single-line and multi-line formats
- Extract sequences by ID or pattern
- Merge multiple FASTA files

Your goal:
Create production-quality file parsing code that handles edge cases and large files efficiently.

Test cases:
- Empty files
- Malformed headers
- Very long sequences
- Files with millions of sequences


## Assignment 4: FASTQ Quality Control

Implement FASTQ quality control pipeline:
- Parse FASTQ files (handle both formats)
- Calculate per-base quality statistics
- Filter reads by quality score
- Trim low-quality ends
- Remove adapter sequences
- Generate quality reports (graphs optional)
- Convert FASTQ to FASTA

Your goal:
Understand next-generation sequencing data and quality assessment.

Requirements:
- Support Phred+33 and Phred+64 encoding
- Implement sliding window quality trimming
- Report before/after statistics
- Handle paired-end reads


## Assignment 5: Sequence Alignment

Implement sequence alignment algorithms:
- Global alignment (Needleman-Wunsch)
- Local alignment (Smith-Waterman)
- Semi-global alignment
- Custom scoring matrices
- Gap penalties (linear and affine)
- Traceback to get actual alignment
- Calculate identity and similarity percentages

Your goal:
Understand dynamic programming and alignment scoring systems.

Bonus:
- Implement banded alignment for similar sequences
- Add support for protein alignment with BLOSUM matrices


## Assignment 6: BioPython Integration

Create a sequence analysis toolkit using BioPython:
- Read sequences from various formats (FASTA, GenBank, EMBL)
- Perform sequence manipulations
- Calculate molecular properties
- Generate restriction enzyme maps
- Perform pairwise alignments
- Access NCBI databases (Entrez)
- Download and parse GenBank records

Your goal:
Master BioPython library and integrate it into real-world workflows.

Features to implement:
- Batch download sequences by accession numbers
- Extract CDS features from GenBank files
- Find restriction sites in a sequence
- Compare sequences and report differences


## Assignment 7: Motif Finder

Develop a sequence motif finding tool:
- Search for exact motifs
- Support IUPAC ambiguity codes
- Use regular expressions for complex patterns
- Find transcription factor binding sites
- Identify restriction enzyme sites
- Support both strands
- Report positions and context
- Calculate motif enrichment

Your goal:
Learn pattern matching in biological sequences and understand regulatory elements.

Patterns to find:
- TATA box: TATAAA
- Kozak sequence: GCCACCATGG
- Poly-A signal: AATAAA
- Common restriction sites


## Assignment 8: Gene Finder

Build a simple gene prediction tool:
- Find all ORFs in all six reading frames
- Filter by minimum length
- Identify start and stop codons
- Calculate protein properties (MW, pI)
- Detect overlapping genes
- Score ORFs by likelihood (codon usage)
- Export results in GFF format

Your goal:
Understand gene structure and implement a basic gene finder algorithm.

Advanced features:
- Predict Shine-Dalgarno sequences (prokaryotes)
- Identify splice sites (eukaryotes, basic)
- Calculate codon adaptation index (CAI)


## Assignment 9: Multiple Sequence Alignment Analyzer

Create tools to analyze multiple sequence alignments:
- Read alignment files (FASTA, Clustal, Stockholm)
- Calculate conservation scores
- Identify conserved regions
- Generate consensus sequence
- Calculate pairwise identities
- Detect gap patterns
- Visualize alignment (text-based)

Your goal:
Work with multiple sequence alignments and understand evolutionary conservation.

Statistics to calculate:
- Column-wise entropy
- Gap percentage per position
- Identity matrix between all sequences
- Most conserved and variable regions


## Assignment 10: Biological Database Interface

Build a command-line tool to interact with biological databases:
- Query NCBI (nucleotide, protein databases)
- Retrieve sequences by ID or search term
- Parse GenBank/GenPept records
- Extract specific features (CDS, genes)
- Download in batch
- Cache results locally
- Export to various formats

Your goal:
Learn to programmatically access biological databases and handle API rate limits.

Features:
- Handle API errors gracefully
- Implement retry logic
- Respect NCBI usage guidelines
- Cache to avoid repeated downloads
- Support query history


## Assignment 11: Sequence Statistics Dashboard

Create a comprehensive sequence analysis dashboard:
- Process multiple sequences from a file
- Calculate extensive statistics:
  * Length distribution
  * GC content distribution
  * k-mer frequencies
  * Codon usage
  * Dinucleotide frequencies
- Generate text-based or simple HTML report
- Support both nucleotide and protein sequences

Your goal:
Build a production-ready analysis tool with comprehensive reporting.

Output format:
- Summary statistics table
- Distribution histograms (ASCII art or real plots)
- Detailed per-sequence report
- Export to CSV/JSON


## Assignment 12: Phylogenetic Analysis Tool

Implement basic phylogenetic analysis:
- Calculate pairwise distances (multiple models)
- Build distance matrix
- Construct phylogenetic tree (UPGMA or NJ)
- Read/write Newick format
- Calculate tree statistics
- Visualize tree (ASCII art)

Your goal:
Understand phylogenetic relationships and tree construction algorithms.

Distance models:
- Hamming distance (p-distance)
- Jukes-Cantor
- Kimura 2-parameter
- Calculate bootstrap support (basic)


## Bonus Project: End-to-End Pipeline

Create a complete sequence analysis pipeline:
1. Download sequences from NCBI for a gene family
2. Perform quality checks
3. Align sequences (multiple alignment)
4. Build phylogenetic tree
5. Identify conserved motifs
6. Predict gene structure
7. Generate comprehensive report

Your goal:
Integrate all learned concepts into a real-world bioinformatics workflow.

This should be a command-line tool with:
- Configuration file support
- Progress reporting
- Error handling
- Logging
- Modular design for easy extension
