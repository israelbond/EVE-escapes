import json
import sqlite3
#script that loads in map_connections.json to eve_system.db


with open ('map_connections.json', 'r') as f:
    jsonMap = json.load(f)    

db = sqlite3.connect('eve_system.db')
c = db.cursor()
count = 0;
for system in jsonMap['systems']:
    cons = ""
    count += 1
    for connection in jsonMap['systems'][system]['connections']:
        cons += connection + " "
    print(cons)
    c.execute("INSERT INTO systems VALUES(?,?,?,?,?)" , (system, jsonMap['systems'][system]['system_name'], jsonMap['systems'][system]['security_status'], jsonMap['systems'][system]['kills'], cons));                        
db.commit()
print(count)
