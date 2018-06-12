# Copyright © 2018 EVE-escapes
# [This program is licensed under the "GNU General Public License"]
# Please see the file LICENSE in the source
# distribution of this software for license terms.

import json
import urllib.request
import requests
import time
#Still need to use time to sort through zkill data. There is more of an hour range in return kill mails. 
#create object to store zkill data in.
class Zkill:
    def __init__(self, zTime, location):
        self.zTime = zTime
        self.location = location

#Print killmails to screen with time, system, and character id. Some kills mails don't have a character_id and I'm unsure of why. Will loop until redisq sever sends a "null package" 
while True:
	while True:
		webUrl = urllib.request.urlopen('https://redisq.zkillboard.com/listen.php') 
		data = webUrl.read()
		jData = json.loads(data.decode('utf-8'))
		#print(jData)
		if jData['package'] is None:
			time.sleep(15)
			print("waiting")
			break
		zTime = jData['package']['killmail']['killmail_time']
		#parts = zTime.split('T')
		#time = parts[1]
		#time = time[:-1]
		#Zkill.time = time
		Zkill.location = jData['package']['killmail']['solar_system_id']
		try:
			print(zTime, Zkill.location, jData['package']['killmail']['victim']['character_id'] )
		except:
			print(zTime, Zkill.location )
