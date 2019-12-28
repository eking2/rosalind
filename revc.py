from pathlib import Path

def revc():

    rev_map = {'A' : 'T',
               'T' : 'A',
               'C' : 'G',
               'G' : 'C'}

    seq = Path('data/rosalind_revc.txt').read_text().strip()

    # reverse complement
    seq = ''.join([rev_map[x] for x in seq])[::-1]

    print(seq)

revc()
