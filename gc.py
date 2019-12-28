from Bio import SeqIO
from io import StringIO

def gc():

    records = SeqIO.parse('data/rosalind_gc.txt', 'fasta')

    # get gc content per record
    gc_dict = {}
    for record in records:

        count_g = record.seq.count('G')
        count_c = record.seq.count('C')

        gc_percent = (count_g + count_c) / len(record.seq) * 100

        gc_dict[record.id] = gc_percent

    # sort and slice to get max gc content
    gc_sorted = sorted(gc_dict.items(), key=lambda x: x[1], reverse=True)
    top_sample = gc_sorted[0][0]
    top_gc = round(gc_sorted[0][1], 5)

    print(top_sample)
    print(top_gc)

gc()

