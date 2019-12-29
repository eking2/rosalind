from pathlib import Path

def hamm():

    seq1, seq2 = Path('data/rosalind_hamm.txt').read_text().splitlines()

    # hamming distance is number of symbols that differ
    dist = sum([1 for s1, s2 in zip(seq1, seq2) if s1 != s2])

    print(dist)

hamm()
