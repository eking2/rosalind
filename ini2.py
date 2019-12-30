from pathlib import Path

def ini2():

    a, b = Path('data/rosalind_ini2.txt').read_text().split()
    a, b = int(a), int(b)

    # calc square of hypotenuse 
    # c^2 = a^2 + b^2
    c_sq = a**2 + b**2

    print(c_sq)

ini2()
