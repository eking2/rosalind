from pathlib import Path
from Bio.Seq import Seq

def ini():

    # load
    input_seq = Path('data/rosalind_ini.txt').read_text()

    # into biopython
    my_seq = Seq(input_seq)

    # count a, c, g, t
    count_a = my_seq.count('A')
    count_c = my_seq.count('C')
    count_g = my_seq.count('G')
    count_t = my_seq.count('T')

    print(count_a, count_c, count_g, count_t)

ini()


