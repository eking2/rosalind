from pathlib import Path
from Bio import Entrez
from Bio import SeqIO
import numpy as np

def frmt():

    samples = Path('data/rosalind_frmt.txt').read_text().split()

    Entrez.email = 'edwking@live.com'

    # get all fastas
    handle = Entrez.efetch(db='nucleotide', id = samples, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))

    # get length of each fasta
    record_lens = []
    for record in records:
        record_lens.append(len(record.seq))

    # find index of shortest sequence
    small_idx = np.argmin(record_lens)

    # print
    print(records[small_idx].format('fasta'))


frmt()





