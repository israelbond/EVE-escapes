#credit goes to https://networkx.github.io/documentation/networkx-1.9/examples/drawing/weighted_graph.html
#sitation goes to networkx documentaion: https://networkx.github.io/documentation/latest/_downloads/networkx_reference.pdf
import matplotlib.pyplot as plt
import networkx as nx
import json
from requests import Session
from collections import OrderedDict
from decimal import Decimal
'''
session = Session()

url = "https://web.cecs.pdx.edu/~briallen/EVE-escapes/HTML_JS/ajax_practice.html"
session.head(url)

response = session.post(
    url = "https://web.cecs.pdx.edu/~briallen/EVE-escapes/HTML_JS/ajax_practice.html",
    data = {
    },
    #header = {
    #    'referer': url
    #}
)
print(response.text)
'''

with open('map_connections.json', 'r') as f:
    universe = json.loads(f.read(), object_pairs_hook=OrderedDict)

G = nx.Graph()

for system in universe['systems']:
    for connection in universe['systems'][system]['connections']:
        w = (float(universe['systems'][connection]['security_status']) - 10.0) * -1
        G.add_edge(universe['systems'][system]['system_name'], universe['systems'][connection]['system_name'], weight = w)

#T =nx.minimum_spanning_tree(G, weight = 'weight', algorithm = 'kruskal', ignore_nan = False)
print(G)
'''
#D = nx.dijkstra_path(T, '30000001', '30001028')
P = nx.dijkstra_path(G, 'Amarr', 'Jita')
count = 0
for e in P:
    count += 1

#print(sorted(T.edges(data=True)))

#sorted(T.edges(data=True))
#print(nx.dijkstra_path(G, 'Amarr', 'Jita'))
print(count)
json.dumps(P) 
print(P)
'''
