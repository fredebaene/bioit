# BioIT

A Python library for all your bioinformatics problems.

## Introduction

Biological macromolecules can be divided into four classes:

- nucleic acids
- proteins
- lipids
- saccharides.

Nucleic acids are polymers, and the monomers making up a nucleic acid are
called nucleotides. Each of these nucleotides consists out of a phosphate
group, a sugar molecule, and a nucleobase. Based on their nucleotides and the
sugar molecule, nucleic acids can be divided into different classes of nucleic
acids, ie. deoxyribonucleic acid (DNA) and ribonucleic acid (RNA):

- DNA
  - double-stranded
  - sugar molecule : deoxyribose
  - base : thymine (T)
- RNA
  - single-stranded
  - sugar molecule : ribose
  - base : uracil (U).

The nucleotides in a single type of nucleic acid differ from each other only in
their nucleobase. Thus, the nucleotides in a single type of nucleic acid can be
uniquely identified and represented by the first letter of the nucleobase they
contain.

As the order of the nucleotides in a nucleic acid matters and each nucleotide
can be represented by a letter, the primary structure of a nucleic acid can be
represented by a string containing only the following letters: 'A', 'C', 'G',
and 'T' ('U' for RNA).

A DNA molecule can be described as follows:

- primary structure : nucleotide sequence
- secondary structure :
  - two strands in opposite directions
  - A binds with T and G binds with C
- tertiary structure : double helix.

## Transcription

A DNA molecule is a double-stranded helix. During transcription, the two
strands are separated and one strand is read in the 3-to-5 direction to form
an mRNA strand. Thus, the mRNA strand is formed in the 5-to-3 direction.

The strand being read during transcription is called the template strand or
antisense strand, the other strand is called the coding strand or sense strand.

As the two DNA strands are complementary, the nucleotide sequence for the mRNA
strand in the 5-to-3 direction is equal to the nucleotide sequence of the
coding strand in the 5-to-3 direction, except that the mRNA molecule contains
uracil (U) instead of thymine (T).

5 - A C G T T T C T C G A C A C G - 3   -> CODING STRAND (SENSE)
    | | | | | | | | | | | | | | |
3 - T G C A A A G A G C T G T G C - 5   -> TEMPLATE STRAND (ANTISENSE)

The above DNA molecule results in the following mRNA molecule:

5 - A C G U U U C U C G A C A C G - 3

## Sequence Class

The Sequence class is the base class used to represent polymers. Polymers are
macromolecules composed of a sequence of identical or similar subunits. If each
of these subunits can be represented by a symbol (or character), then the
polymer can be represented by a string.

Instance variables:

- self.sequence: a string representation of the monomer sequence
- self.label: a label used to identify the polymer molecule

Methods:

- self.monomer_frequencies(self)
  - parameters: no parameters
  - return: a frequency distribution of the monomers
  - return type: dict
- self.calculate_content(self, monomers)
  - parameters:
    - monomers: requires a string object for which the content is to be calculated
  - return: the percentage of monomers in the sequence equaling the given monomers
  - return type: float

## DNA Class



## Vocabulary

- GENOME : THE COMPLETE SET OF AN ORGANISM'S GENETIC INSTRUCTIONS (DNA SEQUENCE)
- SEQUENCE : AN ORDERED COLLECTION OF OBJECTS IN WHICH REPETITIONS ARE ALLOWED
- STRING : A SEQUENCE OF SYMBOLS
- BASE PAIR : THE BONDING OF TWO COMPLEMENTARY BASES (A-T // C-G)
