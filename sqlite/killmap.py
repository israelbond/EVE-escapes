import json
import urllib.request
#open map_connections.json to add kill data
#scipt may be tossed. Don't think its needed anymore
with open('map_connections.json', 'r+') as f:
        universe = json.load(f)
f.close()
count = 0
for sys in universe['systems']:
    if int(universe['systems'][str(sys)]['kills']) > 0:
        count += 1
    universe['systems'][str(sys)]['kills'] = 0
print(count)

#open connection to CCP swagger for kill data
with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
    universe_kills = json.loads(h1.read().decode('utf-8'))
#stitch together map_connections.json and kill data

#zCount and Count are sanity checks to ensure there are the same number of systems with kill data. Looks good so far. 
zCount = 0
for system in universe_kills:
    sys_id = system['system_id']
    universe['systems'][str(sys_id)]['kills'] = system['ship_kills']
    if int(system['ship_kills']) > 0:
        zCount += 1
print(zCount)

with open('map_connections.json', 'w') as jsonFile:
    json.dump(universe , jsonFile)
