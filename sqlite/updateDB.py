import json
import sqlite3
import urllib.request

#updates sqlite database with kill data from CCP
#need to run resetDB.py first to reset kills to zero. 

#open connection to CCP to get kill data
with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
    universe_kills = json.loads(h1.read().decode('utf-8'))

#connect to local .db file
db = sqlite3.connect('eve_system.db')
c = db.cursor()
count = 0;
#updates kills
for system in universe_kills:
    count += 1
    c.execute('''UPDATE systems SET kills = ? WHERE system_id = ?''', (system['ship_kills'], system['system_id']))                        
db.commit()
