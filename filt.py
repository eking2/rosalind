from pathlib import Path
from Bio import SeqIO
from io import StringIO
import numpy as np

def filt():

    lines = Path('data/rosalind_filt.txt').read_text().splitlines()

    # quality threshold, percent of bases above
    threshold, percentage = lines[0].split()
    threshold, percentage = int(threshold), int(percentage)

    # split fastq part of file
    fastq = StringIO('\n'.join(lines[1:]))

    # parse
    records = SeqIO.parse(fastq, 'fastq')

    count = 0
    for record in records:
        # count number above thresh
        arr = np.array(record.letter_annotations['phred_quality'])
        above = np.sum(arr > threshold) 

        # compare to percent of total base cutoff
        if above > len(record.seq) * percentage * (1/100):
            count += 1

    print(count)

filt()


