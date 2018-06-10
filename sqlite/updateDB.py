import json
import sqlite3
import urllib.request
import time
from datetime import datetime
from datetime import timedelta

#updates sqlite database with kill data from CCP and Zkillboard via reisq.zkillboard
#credit for zkillboard

update_time = datetime.now() + timedelta(hours = 1)

with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
	universe_kills = json.loads(h1.read().decode('utf-8'))
#connect to local .db file
db = sqlite3.connect('eve_system.db')
c = db.cursor()
#updates kills
for system in universe_kills:
	c.execute('''UPDATE systems SET kills = ? WHERE system_id = ?''', (system['ship_kills'], system['system_id']))                        
	db.commit()

while True: 
	if datetime.now() >= update_time:
		update_time = datetime.now() + timedelta(hours = 1)
		print("loop hit!")
	#open connection to CCP to get kill data
		with urllib.request.urlopen('https://esi.tech.ccp.is/latest/universe/system_kills/') as h1:
			universe_kills = json.loads(h1.read().decode('utf-8'))
	#connect to local .db file
#		db = sqlite3.connect('eve_system.db')
#		c = db.cursor()
	#updates kills
		for system in universe_kills:
			c.execute('''UPDATE systems SET kills = ? WHERE system_id = ?''', (system['ship_kills'], system['system_id']))                        
			db.commit()
	else:
#		db = sqlite3.connect('eve_system.db')
#		c = db.cursor()
		webUrl = urllib.request.urlopen('https://redisq.zkillboard.com/listen.php')
		data = webUrl.read() 
		jData = json.loads(data.decode('utf-8'))
		if jData['package'] is None:
			time.sleep(60)
			print("waiting..")
		try :
			jData['package']['killmail']['victim']['character_id']
			c.execute('''UPDATE systems SET kills = kills + ? WHERE system_id = ?''', ( 1, jData['package']['killmail']['solar_system_id']))
			db.commit()
			print("zKill")
		except:
			print("issue")
			continue
