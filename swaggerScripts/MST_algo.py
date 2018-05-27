# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
import json
import random
pm = __import__("hashMap")#object representing the imported hash map module


 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of expected vertices
        self.verts = 0 #No. of known vertices
        self.edges = 0#No. of known edges
        self.graph = [] # default dictionary 
                                # to store graph
     
    #This function will contrust the graph that the algorithm will make into a minimal spanning tree
    def CreateGraph(self):
	#opens the map_connections file to read from
        with open('map_connections.json', 'r') as f:
            read_file = json.load(f)

	#will read as many systems as ther are unique keys in the json file
        for items in read_file['systems'].keys():

	    #if the number of vertices created exceeds the expected number of vertices then terminate reading
            if self.verts > self.V - 1:
                break
	    #read in a system id as a source vertex
	    #and subtract the residual 30 million to fit within the bounds
	    #of the graph.
            source = int(read_file['systems'][items]['system_id']) - 30000001

	    #Add one to the known amount of vertexes in the graph
            self.verts += 1

	    #for the adjacent systems(or elements)in the connections array create a new edge to that system
            for adj_sys in read_file['systems'][items]['connections']:
		#perform the same subtraction as was done for the source
                adj_sys = int(adj_sys) - 30000001

	        #temporarily assign a value to the weight of the edge
                weight = random.randint(1, 10)
		
		#if the system id for the adjacent system or the source was greater than
		#the expected number of vertices then omit this edge,
		#else create the edge
                if source > self.V - 1 or adj_sys > self.V - 1:
                    #debug: print("\nPanic: found id", source)
                else:
		    #adds the edge to the graph
                    self.addEdge(int(source), int(adj_sys), int(weight))

    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        self.edges += 1#add one to the number of known edges
        #debug: print("\nsource: ", u, " dest: ", v, " weight: ", w)
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        #print("\n", i)
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's 
        # algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
            # Step 1:  Sort all the edges in non-decreasing 
                # order of their
                # weight.  If we are not allowed to change the 
                # given graph, we can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
 
        parent = [] 
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is equal to V-1
	# i should be never exceed the number of edges
        while e < self.V -1 and i < self.edges - 1:
 
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration

            #debug: print("\n", i)

            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
            # Else discard the edge
 
        # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
 
# Driver code

#create the graph object using the number of systems from hashMap.py
g = Graph(pm.system_tab.num_systems)

#create the graph
g.CreateGraph()
 
print("\nVertices: ",g.verts)
print("\nEdgess: ",g.edges)

#pause scrolling for debug purposes
pm.system_tab.wait()

#Algorithm to builf the minimal spanning tree
g.KruskalMST()
