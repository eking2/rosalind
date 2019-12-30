from Bio import SeqIO
from Bio import motifs
import numpy as np
from collections import Counter

def cons():

    # convert fasta sequences to character array
    arr = np.array([record.seq for record in SeqIO.parse('data/rosalind_cons.txt', 'fasta')])

    # count base pairs per position (column-wise)
    counters = [Counter(col) for col in arr.T]

    # profile matrix from counts
    # shape is [pos, base pair]
    profile_mat = np.array([[counter.get(char, 0) for char in 'ACGT'] for counter in counters])

    # consensus and position counts
    # most_common(n) returns list of tuples containing n top results
    # each tuple is element and counts

    # get most frequent element at each position
    print(''.join([counter.most_common(1)[0][0] for counter in counters]))

    # raw position counts (going down each column of profile matrix)
    for i, char in enumerate('ACGT'):
        print('{}: {}'.format(char, ' '.join(map(str, profile_mat.T[i]))))


def cons2():

    # using biopython motif
    records = SeqIO.parse('data/rosalind_cons.txt', 'fasta')
    m = motifs.create([record.seq for record in records])

    consensus = m.consensus 
    print(consensus)

    # shape is [base pair, pos]
    profile_mat = m.counts

    for i, char in enumerate('ACGT'):
        print('{}: {}'.format(char, ' '.join(map(str, m.counts[char,:]))))


#cons()
cons2()



