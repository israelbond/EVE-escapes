#Eve-Escapes
#map graph hash table

import json

class system:

    def __init__(self, key, connections, sec, kills, name):
        self.key = key
        self.connections
        self.sec = sec
        self.kills = kills
        self.name = name


class Hash:

    def __init__(self, size):
        self.systems = size
        self.hash = []


    def addSystem(self, key, connections, sec, kills, name):
        s.system(key,sec,kills)
     #   for i in range(self.systems):
     #       if 
        self.systems += 1

    def readFile(self):
        with open('map_connections.json', 'r') as f:
            read_file = json.load(f)
            
        for i in read_file['systems']:
            key = read_file['systems'][i]
            for n in read_file['systems'][i]['connections']:
                connections.append(n)

            print(connections)
            sec = read_file['systems'][i]['secureity_status']
            kills = read_file['systems'][i]['kills']
            name = read_file['systems'][i]['system_name']
        self.addSystem(key, connections, sec, kills, name)
            

h = Hash(1)
h.readFile()
