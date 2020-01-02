from Bio import SeqIO
import itertools

def grph():

    # load sequences into dict
    records = SeqIO.parse('data/rosalind_grph.txt', 'fasta')
    records = {record.id : str(record.seq) for record in records}

    # check string overlap of all pairs
    seq_combos = itertools.product(records.keys(), repeat = 2) 

    edges = []
    for seq_combo in seq_combos:
        s1, s2 = records[seq_combo[0]], records[seq_combo[1]]

        # first 3 to last 3 base pairs
        # do not save duplicates
        if s1 != s2 and s1[-3:] == s2[:3]:
            edges.append([seq_combo[0], seq_combo[1]])
    
    for edge in edges:
        print(edge[0], edge[1])

grph()
