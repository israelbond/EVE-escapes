This folder is for our old python scripts and graph algorithms. 

*MST_algo.py and hashMap.py is code generating the graph needed to find a(safe) path through new eden that ended up not being useful. 

*info.json was the original data dump from CCP from procured from Po_huit git hub. Thanks Po!

*killmap.json is an old altered form of map_connections and needs to be removed

*kills.py is a script that uses esipy to get kill data from CCP 

*map.py reads in info.json and adds new fields suchs as kills to and prints it to screen. run python3 map.py >> foo.txt to create new file. Please note there is a hanging curly brace that need to be manually deleted.

*map_connection.json is the working map of the Eve universe that a kill variable for each system has been added.

