from pathlib import Path
import itertools

def perm():

    num = int(Path('data/rosalind_perm.txt').read_text())

    # print all permutations for numbers in range
    perms = list(itertools.permutations(range(1, num+1)))

    print(len(perms))
    for perm in perms:
        print(' '.join(map(str, perm)))

perm()




