from Bio import SeqIO
from collections import Counter
import itertools

def kmer():

    # load sequence
    record = SeqIO.read('data/rosalind_kmer.txt', 'fasta')
    seq = str(record.seq)

    # chunk sequence into 4-mers
    seq_chunks = []
    for i in range(len(seq)):
        sub = seq[i: i+4]
        if len(sub) == 4:
            seq_chunks.append(sub)

    # count 
    counter = Counter(seq_chunks)

    # output counts in lexographic order
    lexos = [''.join(x) for x in (list(itertools.product('AGCT', repeat=4)))]
    lexos = sorted(lexos)

    for lexo in lexos:
        print(counter.get(lexo, 0), end=' ')
    print()


kmer()
