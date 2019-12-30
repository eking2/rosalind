from pathlib import Path
from collections import Counter

def ini6():

    string = Path('data/rosalind_ini6.txt').read_text().split()

    # count number of each word
    counter = Counter(string)
    print(counter)

    for key, val in counter.items():
        print(key, val)

ini6()


