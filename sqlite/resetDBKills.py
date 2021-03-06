# Copyright © 2018 EVE-escapes
# [This program is licensed under the "GNU General Public License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import json
import sqlite3
import urllib.request
#early prototype to reset kill data in the sqlite3 database. Is not longer needed
with open ('../swaggerScripts/map_connections.json', 'r') as f:
    jsonMap = json.load(f)    

with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
    universe_kills = json.loads(h1.read().decode('utf-8'))

db = sqlite3.connect('eve_system.db')
c = db.cursor()
count = 0;
for system in jsonMap['systems']:
    count += 1
    c.execute('''UPDATE systems SET kills = ? WHERE system_id = ?''', (0, system))                        
db.commit()
print(count)
