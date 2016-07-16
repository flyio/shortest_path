# Read GIS Cup format network files as a weighted graph
import networkx as nx
from distance import hubeny, hubeny_seg

def read_giscup(fnode, fedge, fgeom, recalc_length=False):
    # Read node file
    f = open(fnode)
    G = nx.DiGraph()  # This is an empty directed graph
    for line in f:
        row = line.rstrip().split()
        i = int(row[0])
        lat = float(row[1])
        lng = float(row[2])
        G.add_node(i, pos=[lng, lat])

    # Read edge files
    g = open(fedge)
    edges = {}  # temporal
    for line in g:
        row = line.rstrip().split()
        i = int(row[0])
        n1 = int(row[1])
        n2 = int(row[2])
        cost = float(row[3])
        edges[i] = [n1, n2, cost]
        #G.add_edge(n1,n2)

    # Read geometory
    h = open(fgeom)
    for line in h:
        row = line.rstrip().split("^")
        i = int(row[0])
        name = row[1]
        etype = row[2]
        length = int(row[3])
        segments = []
        for j in range((len(row)-4)/2):
            lat = float(row[4 + 2*j])
            lng = float(row[5 + 2*j])
            segments.append([lng, lat])
        if recalc_length:
            length = hubeny_seg(segments)
        G.add_edge(edges[i][0],edges[i][1],cost=edges[i][2],name=name,etype=etype,length=length,segments=segments)
    return G
