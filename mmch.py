from Bio import SeqIO
import math

def mmch():

    record = SeqIO.read('data/rosalind_mmch.txt', 'fasta')
    
    # base counts
    gc_min, gc_max = sorted([record.seq.count('G'), record.seq.count('C')])
    au_min, au_max = sorted([record.seq.count('A'), record.seq.count('U')])

    # number of possible pairings
    gc =  math.factorial(gc_max) // math.factorial(gc_max - gc_min)
    au = math.factorial(au_max) // math.factorial(au_max - au_min)

    # AU combinations * GC combinations
    print(gc * au)

mmch()
