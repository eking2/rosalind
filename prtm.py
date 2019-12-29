from pathlib import Path

# copied from wikipedia
masses = '''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 
'''

def str_to_dict():

    # split on newline, then split on space between
    lines = masses.strip().split('\n')
    masses_dict = {line.split()[0] : float(line.split()[1]) for line in lines}
    
    return masses_dict


def prtm():

    masses_dict = str_to_dict()

    seq = Path('data/rosalind_prtm.txt').read_text().strip()

    mass = 0
    for aa in seq:
        mass += masses_dict[aa]

    print(round(mass, 3))

prtm()

