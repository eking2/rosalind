from pathlib import Path
from Bio import SeqIO
from io import StringIO
import numpy as np

def phre():

    # get threshold, separate fastq data
    lines = Path('data/rosalind_phre.txt').read_text().splitlines()
    thresh = int(lines[0])
    fastq = StringIO('\n'.join(lines[1:]))

    # into biopython
    records = list(SeqIO.parse(fastq, 'fastq'))

    # check average quality score for each record
    # count number of records with average below threshold
    below_thresh = 0
    for record in records:
        if np.mean(record.letter_annotations['phred_quality']) < thresh:
            below_thresh += 1

    print(below_thresh)

phre()

