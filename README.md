# **EVE-escapes**
## Authors:
__Brian Allen: briallen@pdx.edu__  
__Gavin Balakrishnan: gavin4@pdx.edu__  
__Israel Bond: ibond@pdx.edu__   
__Samuel Strba: sstrba@pdx.edu__  
#### Built under a GNU General Public License      

Command line application that supplies support to EVE Online players while they travel through the EVE universe.
Most players could benefit from being able to create a shortest path to a location
based on amount of kills in a system.  

This is the perfect starting point for any EVE mapping development. 
Provides a database built around system_ids and connections using kill data directly fromCCP and zkilboard.
  
### Other software contributions
* Web framework with:
  * CSS
  * JavaScript
  * HTML
    * NOTE: the framework is very simplistic and doesn't interface with the server yet but can be ran to see 
    an example of the layout we were thinking of providing to the users. 
* Kruskal's minimum-spanning-tree algorithm  
  * Was used to build a connected tree with the fewest edges of the least weight for every system in EVE.
    * NOTE: this algorithm didn't work as intended; due to, a the algorithm not being robust enough to produce a path from the tree. Currently path_generator.py is providing a simple dijstra path from one system to another.
     
## Build and install
Markup: *Once the repository is downloaded you can run the updateDB.py using "python3 updateDB.py"to update the databse. Script will continually run and print to screen when data is updated. 
*While the database is being updated, run "python3 path_generator.py 'sys_from' sys_to'". 
*Ex "python3 path_generator Amarr Jita will return the shortest path with no kills from Amarr to Jita and print them to screen. 
*The independent .html files can be run locally produce a web page--unfortunatley we were not able to get a web service up and running. 


The files used in this project are Python3.6 with Networkx library, CSS, HTML, JavaScript, while using JSON files for formatted input.
