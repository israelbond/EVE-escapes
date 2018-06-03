#credit goes to https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html
import matplotlib.pyplot as plt
import networkx as nx
import json
from collections import OrderedDict
with open('map_connections.json', 'r') as f:
    universe = json.loads(f.read(), object_pairs_hook=OrderedDict)

G = nx.Graph()

for system in universe['systems']:
    for connection in universe['systems'][system]['connections']:
        w = int(universe['systems'][connection]['kills'])
        G.add_edge(universe['systems'][system]['system_name'], universe['systems'][connection]['system_name'], weight = w)

T =nx.minimum_spanning_tree(G, weight = 'weight', algorithm = 'kruskal', ignore_nan = False)

#D = nx.dijkstra_path(T, '30000001', '30001028')
P = nx.dijkstra_path(G, 'Amarr', 'Jita')
count = 0
for e in P:
    count += 1

#print(sorted(T.edges(data=True)))

#sorted(T.edges(data=True))
print(nx.dijkstra_path(G, 'Amarr', 'Jita'))
print(count)
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
