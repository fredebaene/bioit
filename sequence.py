# IMPORTING LIBRARIES
# ------------------------------------------------------------------------------
import pandas as pd

# SEQUENCE CLASS
# ------------------------------------------------------------------------------
class Sequence(object):
    """Sequence objects can be used to represent polymers."""

    monomers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    def __init__(self, sequence, label=None):
        self.sequence = sequence
        self.label = label

    @property
    def len(self):
        """The length of the polymer expressed as the number of monomers."""
        return len(self.sequence)

    def monomer_frequencies(self):
        """Returns a frequency distribution of the monomers as a dictionary."""
        frequency_distribution = {}
        for i in self.monomers:
            frequency_distribution[i] = 0
        for i in self.sequence:
            frequency_distribution[i] += 1
        return frequency_distribution

    def calculate_content(self, monomers):
        """Returns how many monomers equal the given monomers as % of total."""
        if not isinstance(monomers, str):
            raise ValueError
        for i in monomers:
            if i not in self.monomers:
                raise ValueError
        frequency = 0
        for i in self.sequence:
            if i in monomers:
                frequency += 1
        content = float(frequency / self.len)
        return content

# DNA CLASS
# ------------------------------------------------------------------------------
class DNA(Sequence):
    """DNA objects can be used to represent DNA sequences/molecules."""

    monomers = 'ACGT'
    complementary_bases = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}

    def transcribe_as_coding_strand(self):
        """Returns the mRNA sequence if this DNA sequence is the coding strand."""
        mrna = ''
        for i in self.sequence:
            if i == 'T':
                mrna += 'U'
            else:
                mrna += i
        return mrna

    def reverse_complement(self):
        """Returns the reverse complement of a DNA sequence."""
        reverse = self.sequence[::-1]
        reverse_complement = ''
        for i in reverse:
            reverse_complement += self.complementary_bases[i]
        return reverse_complement

# RNA CLASS
# ------------------------------------------------------------------------------
class RNA(Sequence):

    monomers = 'ACGU'

if __name__ == '__main__':
    sequence = input('Enter : ')
    monomers = input('Enter monomers : ')
    seq = DNA(sequence)
    print(seq.calculate_content(monomers))
    sequence = input('Enter : ')
    monomers = input('Enter monomers : ')
    seq = DNA(sequence)
    print(seq.calculate_content(monomers))
    sequence = input('Enter : ')
    monomers = input('Enter monomers : ')
    seq = DNA(sequence)
    print(seq.calculate_content(monomers))
