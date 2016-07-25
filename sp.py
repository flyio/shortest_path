#
# add utils/ to the path
import os, sys
sys.path.append(os.getcwd()+"\\utils")

from read_giscup import *
from distance import hubeny

import networkx as nx
from matplotlib import pylab as pl

# Read road network
base = "data/WA_"
G, eid2nodes = read_giscup(base+"Nodes.txt",base+"Edges.txt",
                           base+"EdgeGeometry.txt",True)

# Define heuristic function used in A*
def d(x,y):
    return hubeny(G.node[x]['pos'],G.node[y]['pos'])

# Example of A* search
asp = nx.astar_path(G,1005,2000,heuristic=d,weight='length')
print asp

# Drawing shortest path with pylab
pl.figure()
H = G.subgraph(asp)
posG = nx.get_node_attributes(G,'pos')
nx.draw(G,posG,node_size=1)
posH = nx.get_node_attributes(H,'pos')
nx.draw(H,posH,node_size=1,edge_color='red')
pl.show()

# Showing shortest path property
for i in range(len(asp)-1):
    e = G[asp[i]][asp[i+1]]
    print e['eid'], e['length']
    #print G.node[asp[i]]['pos']
