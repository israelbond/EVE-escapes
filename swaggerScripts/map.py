import json 

with open('info.json', 'r') as f:
        universe = json.load(f)
data = "{\"systems\": {"
for system in universe['systems']:
    data += "\"" + str(system) + "\": { \"system_id\":" + system + ", \"connections\": ["
    for system_stargate in universe['systems'][system]['stargates']:
        system_stargate_string = str(system_stargate)
        if system_stargate != universe['systems'][system]['stargates'][-1]:
            data +=  "\"" + str(universe['stargates'][system_stargate_string]['destination']['system_id']) + "\","
        else:
            data +=  "\"" + str(universe['stargates'][system_stargate_string]['destination']['system_id']) + "\""
    
    data += "], \"kills\" : \"0\"},"
data += "}"
print(data)
        
        
