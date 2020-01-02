from pathlib import Path
from collections import defaultdict

def ddeg():

    edges = Path('data/rosalind_ddeg.txt').read_text().split()
    edges = list(map(int, edges))

    nodes = edges.pop(0)
    num_edges = edges.pop(0)

    # chunk num_edges from flat list to list of edges
    edges = [edges[i: i+2] for i in range(0, len(edges), 2)]

    # adjacency dict
    # node as key
    # list of adjacent nodes as values
    adj = defaultdict(list)
    for node1, node2 in edges:
        adj[node1].append(node2)
        adj[node2].append(node1)

    # double degree of node is number of edges connected to adjacent nodes
    ddegs = defaultdict(int)
    for node in adj:

        # get adjacent nodes
        # add number of edges off the adjacent node
        for edges_to in adj[node]:
            ddegs[node] += len(adj[edges_to])
            
    ddegs = [ddegs.get(i, 0) for i in range(1, nodes+1)]

    print(' '.join(map(str, ddegs)))

ddeg()

