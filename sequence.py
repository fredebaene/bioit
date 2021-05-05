# SEQUENCE CLASS
# ------------------------------------------------------------------------------
class Sequence(object):

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

# DNA CLASS
# ------------------------------------------------------------------------------
class DNA(Sequence):

    monomers = 'ACGT'

# RNA CLASS
# ------------------------------------------------------------------------------
class RNA(Sequence):

    monomers = 'ACGU'
