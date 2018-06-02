#credit goes to https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html
import matplotlib.pyplot as plt
import networkx as nx
import json
from collections import OrderedDict
with open('map_connections.json', 'r') as f:
    input_data = f.read()

universe = json.loads(input_data.decode('utf-8'), object_pairs_hook=OrderedDict)
G = nx.Graph()

for system in universe['systems']:
    print(system)
    for connection in universe['systems'][system]['connections']:
        w = int(universe['systems'][connection]['kills'])
        G.add_edge(system, connection, weight = w)

T =nx.minimum_spanning_tree(G, weight = 'weight', algorithm = 'kruskal', ignore_nan = False)


#print(sorted(T.edges(data=True)))

#sorted(T.edges(data=True))
#print(nx.dijkstra_path(T, '30000001', '30001028'))
#for e in list(G.edges):
#    print(e)
#elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0]
#esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0]
#
#
#
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, node_size= 10)
#nx.draw_networkx_edges(G, pos, edgelist = elarge, width = 2, edge_color='r')
#nx.draw_networkx_edges(G, pos, edgelist = esmall, width = 2, edge_color='b')
#
#nx.draw_networkx_labels(G, pos, font_size= 20, font_family='sans-serif')
#plt.axis('off')
#plt.savefig("weighted_graph.png")
#plt.show()"""
