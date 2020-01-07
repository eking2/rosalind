from Bio import SeqIO
from pathlib import Path

def kmp():

    record = SeqIO.read('data/rosalind_kmp.txt', 'fasta')
    seq = str(record.seq)

    # failure array
    arr = [0] * len(seq)

    # index for start of seq
    # count for current number of matches
    k = 0

    # check if subseq matches suffix 
    # begin search at 2nd char (idx 1)
    # move index forward (k) with match and continue streak
    for i in range(1, len(seq)):

        # reset if hits mismatch while in matching substring
        while k > 0 and seq[k] != seq[i]:
            # slide back, using record of previous prefixes to restart count
            k = arr[k-1]

        # hits match, push up index
        if seq[k] == seq[i]:
            k+= 1

        arr[i] = k

    out = (' '.join(map(str, arr)))
    print(out)
    #Path('kmp.txt').write_text(out)


kmp()
