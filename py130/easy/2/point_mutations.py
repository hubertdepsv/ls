class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, other_strand):
        length = min(len(self.strand), len(other_strand))
        original_strand = self.strand[:length]
        other_strand = other_strand[:length]

        differences = 0
        for index in range(length):
            if original_strand[index] != other_strand[index]:
                differences += 1
        
        return differences