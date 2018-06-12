This folder is for our python scripts and graph algorithms. The no_longer_relevant folder contains protypes and some features that didn't pan out 

*map_connection.json is the working map of the Eve universe that a kill variable for each system has been added. Special thank to Po_huit to putting the orginal data dump together

*path_generator.py uses the networkx library to create a graph of the eve universe, gets kill data from the eve_system.db then runs a dijkstra algorithm to find the shortest kill free path from one system to another.
