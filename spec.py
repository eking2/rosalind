from pathlib import Path
import numpy as np

mass_table = '''A   71.03711
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
Y   163.06333'''


def spec():

    # make dict of masses
    atoms = mass_table.split()[::2]
    masses = mass_table.split()[1::2]
    mass_dict = {atom:float(mass) for atom, mass in zip(atoms, masses)}

    # load spectrum
    spec = Path('data/rosalind_spec.txt').read_text().splitlines()
    spec = np.array(spec, dtype=float)

    # get mass differences
    diffs = spec[1:] - spec[:-1]

    # get closest mass value from mass_dict to each difference
    # find min abs difference at each
    prot = []
    for diff in diffs:
        mass_diff = {}
        for aa, aa_mass in mass_dict.items():
            mass_diff[aa] = np.abs(diff - aa_mass)

        # sort and print
        prot.append(sorted(mass_diff.items(), key= lambda x: x[1])[0][0])

    print(''.join(prot))

spec()


