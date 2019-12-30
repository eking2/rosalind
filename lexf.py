from pathlib import Path
import itertools

def lexf():

    symbols, length = Path('data/rosalind_lexf.txt').read_text().splitlines()
    symbols = symbols.split()
    length = int(length)

    # cartesian product
    combos = list(itertools.product(symbols, repeat=length))
    combos = sorted(combos)

    for combo in combos:
        print(''.join(combo))


lexf()

