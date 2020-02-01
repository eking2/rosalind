from pathlib import Path

def tree():

    # tree with n nodes has n-1 edges
    # solve with n - 1
    record = Path('data/rosalind_tree.txt').read_text().splitlines()
    
    # number of nodes from first line
    nodes = int(record[0])

    # number of edges from rest of file
    num_edges = len(record[1:])

    print(nodes - num_edges - 1)


tree()

