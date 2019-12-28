from Bio import SeqIO

def rvco():

    records = SeqIO.parse('data/rosalind_rvco.txt', 'fasta')

    matches = 0
    # compare rev complement to original sequence
    for record in records:
        if record.seq.reverse_complement() == record.seq:
            matches += 1

    print(matches)

rvco()
