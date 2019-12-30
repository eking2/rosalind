from Bio import SeqIO
import itertools

def lcsm():

    # find shortest shared motif
    records = SeqIO.parse('data/rosalind_lcsm.txt', 'fasta')
    seqs = [record.seq for record in records]

    # start with shortest sequence
    shortest = str(min(seqs, key=len))
    
    # delete last base pair 
    # delete starting base pair 
    # until find match with all other sequences
    #for seq_len in range(len(shortest), 0, -1):
    #    for start in range(len(shortest) - seq_len + 1):
    #        substring = shortest[start : start+seq_len]

    # sort substrings by descending length
    #substrings = sorted(substrings, key=len, reverse=True)
    #print(substrings)

    # get all possible substrings from shortest sequence in descending order
    #substrings = [''.join(sub) for i in range(len(shortest)) for sub in itertools.combinations(shortest, i+1)]
    #for i in range(len(shortest)):
    #    for sub in itertools.combinations(shortest, i+1):
    #        substring = ''.join(sub)
    #        print(substring)

        # loop over substrings to find match
    #        if all(substring in seq for seq in seqs):
    #            break
    
    # get all substrings from shortest sequence in descending order
    seq_len = len(shortest)
    substrings = [shortest[x:y] for x, y in itertools.combinations(range(seq_len + 1), r=2)]
    substrings = sorted(substrings, key=len, reverse=True)

    # check for matches
    for substring in substrings:
        if all(substring in seq for seq in seqs):
            print(substring)
            break

lcsm()
