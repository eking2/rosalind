from pathlib import Path
from io import StringIO
from Bio import SeqIO
import numpy as np

def bphr():

    lines = Path('data/rosalind_bphr.txt').read_text().splitlines()

    # extract thresh and separate fastq
    thresh = int(lines[0])
    fastq = StringIO('\n'.join(lines[1:]))

    records = list(SeqIO.parse(fastq, 'fastq'))

    for i, record in enumerate(records):
        
        # get quality at each position
        phred = np.array(record.letter_annotations['phred_quality'])

        # add together, if first record then save as new array
        if i == 0:
            phreds = phred
        else:
            phreds += phred

    # average quality at each position
    phreds_avg = phreds / len(records)

    # sum number of positions below thresh
    print(sum(phreds_avg < thresh))

bphr()

