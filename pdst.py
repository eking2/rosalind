from Bio import SeqIO
import itertools

def pdst():

    records = [x.seq for x in SeqIO.parse('data/rosalind_pdst.txt', 'fasta')]
    num_records = len(records)

    # all pairs of sequences
    combos = itertools.product(records, records)
    for i, combo in enumerate(combos):
        
        seq_len = len(combo[0])

        # count number of base pair matches
        matches = 0
        for s1, s2 in zip(combo[0], combo[1]):
            if s1 == s2:
                matches += 1

        # calc mismatch distance between strings
        distance = '{:.5f}'.format(1 - (matches / seq_len))

        # print matrix, newline after each full pass
        if i % num_records == 0 and i != 0:
            print()
            print(distance, end=' ')
        else:
            print(distance, end=' ')

    print()


pdst()
