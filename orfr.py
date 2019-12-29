from pathlib import Path
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def orfr():

    # find longest possible amino acid sequence starting from ATG
    # check forward and reverse
    seq = Seq(Path('data/rosalind_orfr.txt').read_text().strip(), generic_dna)
    rseq = seq.reverse_complement()

    '''
    1. translate all 6 reading frames (3 forward, 3 rev) 
    2. find sequences starting with MET
    3. split on stop codon (*)
    4. remove sequences that do not start with M (resulting from split on stop codon)
    5. get lengths and select max
    '''

    max_len = 0
    all_translated = []
    for i in range(3):
        for dna_seq in [seq, rseq]:

            # copy with reading frame set
            dna_copy = dna_seq[i:]

            # remove tail base pairs if dna copy is not multiple of 3
            if len(dna_copy) % 3 != 0:
                to_cut = len(dna_copy) % 3
                dna_copy = dna_copy[:-to_cut]

            # first split on M
            # keep the delimeter M that is removed 
            # then split on stop
            # will result in sequences that do not start with M, clean up in next step
            translated = [Seq('M' + str(x)).split('*') for x in dna_copy.translate().split('M')]

            # flatten list of lists and drop sequences not starting with M
            translated = sum(translated, [])
            translated = [x for x in translated if x.startswith('M')]
            all_translated.extend(translated)

    # get max length and seq
    for trans_seq in all_translated:
        if len(trans_seq) > max_len:
            max_len = len(trans_seq)
            max_seq = trans_seq

    print(max_seq)

orfr()
