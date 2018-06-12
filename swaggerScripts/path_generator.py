# Copyright © 2018 EVE-escapes
# [This program is licensed under the "GNU General Public License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

#citation goes to networkx documentaion: https://networkx.github.io/documentation/latest/_downloads/networkx_reference.pdf
import networkx as nx
import json
import sqlite3
import sys
'''Hard coded sqlite colums into setting up the graph. Need to create class to put query into dict.
	col[0] sys_id 
	col[1] sys_name 
	col[2] security_rating 
	col[3] system_kills 
	col[4] sys_connections
'''
#get args from command line
from_sys = sys.argv[1]
to_sys = sys.argv[2]

#Needed dictionary for name data. Is a hackjob, I know. 
with open('map_connections.json', 'r') as h1:
	universe = json.load(h1)

#get data from sqlite DB
db = sqlite3.connect('../sqlite/eve_system.db')
c = db.cursor()
data = c.execute('''SELECT * FROM systems''')

#build graph for dijkstra path
G = nx.Graph()
for system in data:
	connections = str.split(system[4])
	for connection in connections:
		w = int(system[3])
		G.add_edge(system[1], universe['systems'][connection]['system_name'], weight = w)
try:
	P = nx.dijkstra_path(G, from_sys, to_sys)
	json.dumps(P) 
	print(P)
except:
	print("Invalid systems entered. Please try again")


