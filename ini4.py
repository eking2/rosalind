from pathlib import Path

def ini4():

    a, b = Path('data/rosalind_ini4.txt').read_text().split()
    a, b = int(a), int(b)

    # sum all odd integers between a and b
    result = sum(x for x in range(a, b+1) if x % 2 == 1)
    print(result)

ini4()
