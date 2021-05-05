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

## Sequence Class

The Sequence class is the base class used to represent polymers. Polymers are
macromolecules composed of a sequence of identical or similar subunits. If each
of these subunits can be represented by a symbol (or charachter), then the
polymer can be represented by a string.

## DNA Class

Instance variables:

- self.sequence: a string representation of the nucleotide sequence
- self.label: a label used to identify the DNA segment

## Vocabulary

- GENOME : ALL OF THE DNA CONTAINED IN AN ORGANISM'S CHROMOSOMES
- SEQUENCE : AN ORDERED COLLECTION OF OBJECTS IN WHICH REPETITIONS ARE ALLOWED
- STRING : A SEQUENCE OF SYMBOLS
