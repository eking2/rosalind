from pathlib import Path
from Bio.Seq import translate

def ptra():

    dna, prot = Path('data/rosalind_ptra.txt').read_text().splitlines()

    # no table 7, 8
    code_tables = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

    # test all possible translation tables, break on match
    for code_table in code_tables:

        # ignore stop codons
        aa_seq = translate(dna, table=code_table, stop_symbol = '', to_stop=False)

        if aa_seq == prot:
            print(code_table)
            break

ptra()
