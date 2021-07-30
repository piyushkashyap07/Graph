# Dijkstra's Algorithm
# Send Feedback
# Given an undirected, connected and weighted graph G(V, E) with V number of vertices(which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex(i.e. Vertex 0) to all other vertices(including source vertex also) using Dijkstra's Algorithm.
# Input Format:
# Line 1: Two Integers V and E(separated by space)
# Next E lines: Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi(separated by space)
# Output Format:
# For each vertex, print its vertex number and its distance from source, in a separate line. The vertex number and its distance needs to be separated by a single space.
# Note: Order of vertices in output doesn't matter.
# Constraints:
# 2 <= V, E <= 10 ^ 5
# Time Limit: 1 sec
# Sample Input 1:
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1:
# 0 0
# 1 3
# 2 4
# 3 5






import sys


class graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.adjmatrix = [[0 for i in range(nvertices)]
                          for j in range(nvertices)]

    def addedge(self, v1, v2, wt):
        self.adjmatrix[v1][v2] = wt
        self.adjmatrix[v2][v1] = wt

    def __bfs(s, visited):
        q = queue.Queue()
        q.put(s)
        visited[s] = True
        while q.empty() is False:
            front = q.get()
            print(front)
            for i in range(self.nvertices):
                if self.adjmatrix[front][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs():
        visited = [False for i in range(self.nvertices)]
        for i in range(self.nvertices):
            if visited[i] is False:
                self.__bfs(i, visited)

    def __getminvertex(self, visited, weight):
        minVertex = -1
        for i in range(self.nvertices):
            if(visited[i] is False and (minVertex == -1 or (weight[minVertex] > weight[i]))):
                minVertex = i
        return minVertex

    def prism(self):
        visited = [False for i in range(self.nvertices)]
         parent = [-1 for i in range(self.nvertices)]
          weight = [sys.maxsize for i in range(self.nvertices)]
           for i in range(self.nvertices-1):
                minvertex = self.__getminvertex(visited, weight)
                visited[minvertex] = True
                for j in range(self.nvertices):
                    if self.adjmatrix[minvertex][j] > 0 and visited[j] is False:
                        if weight[j] > self.adjmatrix[minvertex][j]:
                            weight[j] = self.adjmatrix[minvertex][j]
                            parent[j] = minvertex
            for i in range(1, self.nvertices):
                if parent[i] > i:
                    print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
                else:
                    print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))

    def __getminvertexd(self, visited, weight):
        minVertex = -1
        for i in range(self.nvertices):
            if(visited[i] is False and (minVertex == -1 or (weight[minVertex] > weight[i]))):
                minVertex = i
        return minVertex

    def djikstra(self):
        visited = [False for i in range(self.nvertices)]
        dist = [sys.maxsize for i in range(self.nvertices)]
        dist[0] = 0
        for i in range(self.nvertices-1):
            minvertex = self.__getminvertexd(visited, dist)
            visited[minvertex] = True
            for j in range(self.nvertices):
                if self.adjmatrix[minvertex][j] > 0 and visited[j] is False:
                    if dist[j] > dist[minvertex] + self.adjmatrix[minvertex][j]:
                        dist[j] = dist[minvertex] + \
                            self.adjmatrix[minvertex][j]
        for i in range(self.nvertices):
            print(str(i) + " " + str(dist[i]))

    def removeedge(self, v1, v2):
        if not self.containsedge(v1, v2):
            return
        self.adjmatrix[v1][v2] = 0
        self.adjmatrxi[v2][v2] = 0

    def containsedge(self, v1, v2):
        return True if self.adjmatrix[v1][v2] > 0 else False


li = [int(x) for x in input().split()]
n = li[0]
e = li[1]
g = graph(n)
for i in range(e):
    curr = [int(x) for x in input().split()]
    g.addedge(curr[0], curr[1], curr[2])
g.djikstra()
