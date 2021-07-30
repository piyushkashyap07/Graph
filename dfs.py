class graph:
    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix=[[0 for i in range(nvertices)] for j in range(nvertices)]

    def addedge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1
    
    def removeedge(self,v1,v2):
        if self.containedge(v1,v2) is False:
            return
        self.adjmatrix[v1][v2] = 0
        self.adjmatrix[v2][v1] = 0

    def __helperdfs(self,sv,visited):
        print(sv)
        visited[sv]=True
        for i in range(self.nvertices):
            if self.adjmatrix[sv][i]>0 and visited[i] is False:
                self.__helperdfs(i,visited)

    def dfs(self):
        visited = [False for i in range(self.nvertices)]
        self.__helperdfs(0, visited)


    def containedge(self,v1,v2):
        return True if self.adjmatrix[v1][v2]>0  else False
    
    def __str__(self):
        return str(self.adjmatrix)
g=graph(5)
g.addedge(0,1)    
g.addedge(1,3)    
g.addedge(2,4)
g.addedge(2,3)
g.addedge(0,2)
g.dfs()   

