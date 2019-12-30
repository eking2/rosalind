from pathlib import Path

def ini3():

    string, nums = Path('data/rosalind_ini3.txt').read_text().splitlines()
    a, b, c, d = map(int, nums.split())

    # print slice [a:b+1], [c:d+1]
    print(string[a : b+1], string[c: d+1])

ini3()
