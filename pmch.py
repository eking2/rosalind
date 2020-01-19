from Bio import SeqIO
from math import factorial

def pmch():

    record = SeqIO.read('data/rosalind_pmch.txt', 'fasta')

    # count number of GC and AU pairs
    # basepair edges
    gc = record.seq.count('G')
    au = record.seq.count('A')

    matches = factorial(gc) * factorial(au)

    print(matches)

pmch()
