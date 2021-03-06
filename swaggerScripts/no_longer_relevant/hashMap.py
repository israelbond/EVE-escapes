#Eve-Escapes
#map graph hash table

import json
connections =[]


class table:
	
	def __init__(self, size):
	    self.num_systems = size
	    self.num_connections = size
	    self.systemsDic = {}
	
	
	def addSystem(self, key, connections, sec, kills, name):
	    if key not in self.systemsDic:
	    	self.systemsDic[key] = key
	    	#self.systemsDic[key] += sec
	    	#self.systemsDic[key] += kills
	    	#self.systemsDic[key] += name
	    	#print("\nKey = ", key)
	    	self.num_systems += 1

	def readFile(self):
	    with open('map_connections.json', 'r') as f:
	        read_file = json.load(f)
	        
	    for i in read_file['systems']:
	        if (int(read_file['systems'][i]['system_id']) - 30000001) < 5216:
	            key = str(read_file['systems'][i])
	            for n in read_file['systems'][i]['connections']:
	                str(connections.append(n))
	                self.num_connections += 1
	            sec = str(read_file['systems'][i]['security_status'])
	            kills = read_file['systems'][i]['kills']
	            name = read_file['systems'][i]['system_name']
	            self.addSystem(key, connections, sec, kills, name)

	    f.close()

	def wait(self):
		i = 0
		while i < 100000000:
			i += 1
	
	def print_table(self):
		for i in self.systemsDic:
			print("\n ", i)
			#self.wait()

	def find_kills(self, key):
	    for i in self.systemsDic:
	        if key not in self.systemsDic:
	           break
	        if i == key:
	           return self.systemsDic['systems'][i]['kills']
 


#main
#declaration of the adj list and pertanent information for each system
system_tab = table(1)
#Read teh Json file with all system information and create a dictionary
system_tab.readFile()
#Print the number of systems
#system_tab.print_table()
print("\n", system_tab.num_systems)
print("\n", system_tab.num_connections)


