from pathlib import Path
import itertools

def sign():

    n = int(Path('data/rosalind_sign.txt').read_text())

    # get all positive and negative digits
    digits = list(range(-n, n+1))
    digits.remove(0)

    # all permutations
    permutations = itertools.permutations(digits, n)

    # remove combos where abs(num) is duplicated
    # keep only combos with set size == n
    combos = []
    for perm in permutations:
        if len(set(map(abs, perm))) == n:
            combos.append(perm)

    out = []
    out.append(len(combos))
    #print(len(combos))
    for combo in combos:
        #print(*combo)
        out.append(' '.join(map(str, combo)))

    Path('sign.txt').write_text('\n'.join(map(str, out)))



sign()


