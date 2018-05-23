#Eve-Escapes
#map graph hash table

import json
connections =[]


class table:
	
	def __init__(self, size):
	    self.num_systems = size
	    self.systemsDic = {}
	
	
	def addSystem(self, key, connections, sec, kills, name):
	    if key not in self.systemsDic:
	    	self.systemsDic[key] = connections
	    	self.systemsDic[key] += sec
	    	self.systemsDic[key] += kills
	    	self.systemsDic[key] += name
	    	#print("\nKey = ", key)
	    	self.num_systems += 1

	def readFile(self):
	    with open('map_connections.json', 'r') as f:
	        read_file = json.load(f)
	        
	    for i in read_file['systems']:
	        key = str(read_file['systems'][i])
	        for n in read_file['systems'][i]['connections']:
	            str(connections.append(n))
	        sec = str(read_file['systems'][i]['security_status'])
	        kills = read_file['systems'][i]['kills']
	        name = read_file['systems'][i]['system_name']
	        self.addSystem(key, connections, sec, kills, name)

	    f.close()

	def print_table(self):
		for i in self.systemsDic:
			print("\n ", i)

	def find_Sec(self, key):
	    for i in self.systemsDic:
	        if key not in self.systemsDic:
	           break
	        if i == key:
	           return self.systemsDic['systems'][i]['security_status']
 


#main
#declaration of the adj list and pertanent information for each system
system_tab = table(1)
#Read teh Json file with all system information and create a dictionary
system_tab.readFile()
#Print the number of systems
system_tab.print_table()
#print("\n", system_tab.systems)


