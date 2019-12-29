from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO

def bfil():

    # read input and split threshold from fastq lines
    lines = Path('data/rosalind_bfil.txt').read_text().splitlines()
    thresh = int(lines[0])
    seqs = StringIO('\n'.join(lines[1:]))

    records = SeqIO.parse(seqs, 'fastq')
    clean_records = []

    # compare sequences at start and end to threshold
    # at first high quality base, stop count
    for record in records:

        # loop over front
        for i, quality in enumerate(record.letter_annotations['phred_quality']):
            front_cut = i
            if quality >= thresh:
                break

        # loop over back
        for i, quality in enumerate(record.letter_annotations['phred_quality'][::-1]):
            back_cut = i
            if quality >= thresh:
                break


        # save trimmed to new SeqRecord by slicing with cut indexes
        # keep all metadata

        # back_cut condition if back_cut == 0, then will not select any sequence
        if back_cut == 0:
            clean_seq = record.seq[front_cut : ]
            clean_quals = record.letter_annotations['phred_quality'][front_cut : ]
        else:
            clean_seq = record.seq[front_cut : -back_cut]
            clean_quals = record.letter_annotations['phred_quality'][front_cut : -back_cut]

        clean_record = SeqRecord(clean_seq, id=record.id, name=record.name, description=record.description)
        clean_record.letter_annotations['phred_quality'] = clean_quals
        clean_records.append(clean_record)

    output = StringIO()
    SeqIO.write(clean_records, output, 'fastq')
    print(output.getvalue().strip())
    #SeqIO.write(clean_records, 'text.fastq', 'fastq')

bfil()
