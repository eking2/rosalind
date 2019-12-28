from Bio import SeqIO
from io import StringIO

def tfsq():

    # read in fastq and convert to fasta
    # do not save output, print in terminal
    handle = StringIO('')

    SeqIO.convert('data/rosalind_tfsq.txt', 'fastq', handle, 'fasta')

    print(handle.getvalue())
    

tfsq()
