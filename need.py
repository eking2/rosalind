from pathlib import Path
from Bio import Entrez
from Bio import SeqIO
from Bio import pairwise2

def need():

    samples = Path('data/rosalind_need.txt').read_text().split()

    # get fasta
    Entrez.email = 'edwking@live.com'
    handle = Entrez.efetch(db='nucleotide', id=samples, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))

    # align
    # +5/-4 is same as EDNAfull
    align = pairwise2.align.globalms(records[0], records[1], 5, -4, -10, -1, 
                                     penalize_extend_when_opening=True, penalize_end_gaps=True)
    #print(pairwise2.format_alignment(*align[0]))
    print(align[0][2])

need()


