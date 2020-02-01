from pathlib import Path

def inod():

    # unrooted binary tree with n leaves has n-2 internal nodes
    leaves = int(Path('data/rosalind_inod.txt').read_text())

    print(leaves - 2)

inod()


