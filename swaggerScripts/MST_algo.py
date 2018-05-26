# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
import json
import random
pm = __import__("hashMap")


 
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.verts = 0
        self.edges = 0
        self.graph = [] # default dictionary 
                                # to store graph
         
    def CreateGraph(self):
        with open('map_connections.json', 'r') as f:
            read_file = json.load(f)

        for items in read_file['systems'].keys():
            if self.verts > self.V - 1:
                break
            source = int(read_file['systems'][items]['system_id']) - 30000001
            self.verts += 1
            weight = random.randint(1, 10) #float(read_file['systems'][items]['security_status'])
            for adj_sys in read_file['systems'][items]['connections']:
                adj_sys = int(adj_sys) - 30000001
                #if source > self.V - 1:
                #   print("\nPanic: found id", source)
                #   source = random.randint(0, self.V-1)
                #if adj_sys > self.V - 1:
                #   print("\nPanic: found id", adj_sys)
                #   adj_sys = random.randint(0, self.V-1)
                #else:
                #self.addEdge(int(source), int(adj_sys), int(weight))
                if source > self.V - 1 or adj_sys > self.V - 1:
                    print("\nPanic: found id", source)
                else:
                    self.addEdge(int(source), int(adj_sys), int(weight))

    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        self.edges += 1
        #print("\nsource: ", u, " dest: ", v, " weight: ", w)
 
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
        while e < self.V -1 and i < self.edges - 1:
 
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
            print("\n", i)
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
g = Graph(pm.system_tab.num_systems)

g.CreateGraph()
 
print("\nVertices: ",g.verts)
pm.system_tab.wait()

g.KruskalMST()
 
