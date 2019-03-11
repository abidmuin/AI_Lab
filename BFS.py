# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:58:22 2019

@author: muin
"""

from collections import defaultdict

class Graph:
    
    #Constructor
    def __init__(self):
        #default dictionary to store graph
        self.graph = defaultdict(list)
    
    #function to add edge to graph
    def addEdge(self, u,v):
        self.graph[u].append(v)
        
    #function to print a bfs of graph
    def bfs(self, s):
        #mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        #create a queue for bfs
        queue = []
        #mark source node as visited and enqueue it 
        queue.append(s)
        visited[s] = True
        
        while queue:
            #dequeue a vertex from queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            
            for i in self. graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
                    
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print ("Following is BFS" " (Starting from vertex 2)")

g.bfs(2)