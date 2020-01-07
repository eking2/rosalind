from Bio import SeqIO
from Bio.Seq import Seq
import re

def orf():

    # find all coding sequences (with start and stop codon) in the 6 reading frames
    record = SeqIO.read('data/rosalind_orf.txt', 'fasta')
    seq = str(record.seq)
    rev = str(record.seq.reverse_complement())

    # DNA stop codons 
    # TAG, TGA, TAA

    # lookahead for overlapping
    # begins with start
    # wildcard in between, multiple of 3, lazy
    # ends with stop
    # check forward and reverse
    match_f = re.findall('(?=(ATG(?:.{3})*?(TAG|TGA|TAA)))', seq)
    match_r = re.findall('(?=(ATG(?:.{3})*?(TAG|TGA|TAA)))', rev)

    # translate matches 
    # match returns tuple of groups
    matches = match_f + match_r
    match_translated = []
    for group1, group2 in matches:
        translated = Seq(group1).translate(to_stop=True)

        # do not print duplicates
        if translated not in match_translated:
            match_translated.append(translated)
            print(translated)

orf()
    

