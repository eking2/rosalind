from pathlib import Path
from collections import Counter

def dna():

    seq = Path('data/rosalind_dna.txt').read_text()

    count = Counter(seq)
    #count_a = seq.count('A')
    #count_t = seq.count('T')
    #count_c = seq.count('C')
    #count_g = seq.count('G')

    #print(count_a, count_c, count_g, count_t)
    print(count['A'], count['C'], count['G'], count['T'])

dna()
    
