# Code: BFS Traversal
# Send Feedback
# Given an undirected and disconnected graph G(V, E), print its BFS traversal.
# Note:
# 1. Here you need to consider that you need to print BFS path starting from vertex 0 only.
# 2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# 3. E is the number of edges present in graph G.
# 4. Take graph input in the adjacency matrix.
# 5. Handle for Disconnected Graphs as well
# Input Format:
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.
# Output Format:
# Print the BFS Traversal, as described in the task.
# Constraints:
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# 0 1 3 2
import queue
q = queue.Queue()
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.AdjacenyMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        
    def addentry(self,v1,v2):
        self.AdjacenyMatrix[v1][v2] = 1
        self.AdjacenyMatrix[v2][v1] = 1
        
    def deleteentry(self,v1,v2):
        if self.containedges(v1,v2) is False:
            return
        self.AdjacenyMatrix[v1][v2] = 0
        self.AdjacenyMatrix[v2][v1] = 0
        
    def __dfsHelper(self,sv,visited):
        
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.AdjacenyMatrix[sv][i] > 0 and visited[i] == False:
                self.__dfsHelper(i,visited)
        
    def dfs(self):
        sv = 0
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(sv,visited)
        
    def __bfsHelper(self,sv,visited): 
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            vertex = q.get()
            print(vertex,end=' ')
            for i in range(self.nVertices):
                if self.AdjacenyMatrix[vertex][i] > 0 and visited[i] == False:
                    q.put(i)
                    visited[i] = True
    
    def bfs(self):
        sv = 0
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i,visited)
        
    def containedges(self,v1,v2):
        return True if self.AdjacenyMatrix[v1][v2] == 1 else  False
        
    def __str__(self):
        return str(self.AdjacenyMatrix)
    
    

VE = [int(i) for i in input().split()]
n = VE[0]
e = VE[1]
g = Graph(n)
while e > 0:
    edges = [int(i) for i in input().split()]
    g.addentry(edges[0],edges[1])
    e = e - 1

g.bfs()