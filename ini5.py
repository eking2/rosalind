from pathlib import Path

def ini5():

    lines = Path('data/rosalind_ini5.txt').read_text().splitlines()

    # print even numbered lines
    # assume 1-based numbering for this problem
    for i, line in enumerate(lines, 1):
        if i % 2 == 0:
            print(line)

ini5()

