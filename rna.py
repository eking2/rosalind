from pathlib import Path

def rna():

    seq = Path('data/rosalind_rna.txt').read_text()

    seq = seq.replace('T', 'U')

    print(seq)

rna()
