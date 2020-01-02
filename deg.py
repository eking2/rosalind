from pathlib import Path
from collections import Counter

def degs():

    
    edge_list = Path('data/rosalind_deg.txt').read_text().split()
    edge_list = list(map(int, edge_list))

    nodes = edge_list.pop(0)
    edges = edge_list.pop(0)
    
    # from edge list get degree of each vertex
    # count the edges
    counter = Counter(edge_list)

    # no 0 node
    degrees = [counter[i] for i in range(1, len(counter) + 1)]

    print(' '.join(map(str, degrees)))

degs()
