* You'll need to install sqlite to access the eve_system.db
* I recomened get sqlitebrowser to set up the DB and browse the data
* resetDB.py resets all the kills to 0 was used for testing
* updateDB.py updates kills from CCP (data is only updated hourly) and Zkillboard via redisQ.
* eve_system.db is the sqlite3 file that contain eve system data
* map_connection.json was orginal file used before the transfer to sqlite database. Is still needed for updateDB.py unfortunatley.
*zkill_prototype.py was the orginal script for pulling zkillboard data from redisq
*jsonMapToDB.py added map_connections.json to sqlite database
