from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
from io import StringIO

def splc():

    records = SeqIO.parse('data/rosalind_splc.txt', 'fasta')

    # convert to regular string and replace 
    for i, record in enumerate(records):
        if i == 0:
            # first record is template, rest are introns to remove
            template = str(record.seq)
            continue

        template = template.replace(str(record.seq), '')

    # back to seq and translate
    # do not include * for stop
    aa_seq = Seq(template, generic_dna).translate(to_stop=True)

    print(aa_seq)


splc()
