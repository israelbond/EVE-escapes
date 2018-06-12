This folder is for our python scripts and graph algorithms. The no_longer_relevant folder contains protypes and some features that didn't pan out 

*MST_algo.py and hashMap.py is code generating the graph needed to find a(safe) path through new eden

*info.json was the original data dump from CCP from procured from Po_huit git hub. Thanks Po!

*killmap.json is an old altered form of map_connections and needs to be removed

*kills.py is a script that uses esipy to get kill data from CCP 

*loops_practice.html is the driver of the load_file.js code. Sets up basic body of html then uses load_file.js

*load_file.js reads from the file map_connections loops through and adds each name, system_id, and the systems connection into the driving HTML table. 

*map.py reads in info.json and adds new fields suchs as kills to and prints it to screen. run python3 map.py >> foo.txt to create new file. Please note there is a hanging curly brace that need to be manually deleted.

*map_connection.json is the working map of the Eve universe that a kill variable for each system has been added.

*newKills.py  stitches together map_connections.json and kill data from CCP API.

*zkill.py pings redisq sever for zkill mails and print them to screen. Data still needs to be scrubbed for kill mails in the past hour. 
