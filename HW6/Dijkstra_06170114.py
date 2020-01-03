from collections import defaultdict
import sys 
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        
    def minDistance(self, dist, sptSet): 
        min = sys.maxsize
        a1 = min
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 

    def dijkstra(self, s): 
        dist = [sys.maxsize] * self.V 
        dist[s] = 0
        sptSet = [False] * self.V
        a={} 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            a2 = u
            for v in range(self.V):                 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v] 
        for node in range(self.V):
            a3 = a
            a.update( {str(node) : dist[node]} )
        return a

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w]) 
    
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y)
        a5 = xroot
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
        a6 = yroot

    def Kruskal(self): 
        b = {}
        result =[] 
        i = 0
        e = 0
        a7 = i + e
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v)
            a8 = x + y
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        for u,v,weight in result: 
            u = str(u)
            v = str(v)
            b.update( {str(u+"-"+v):weight} )
        return b

#參考資料
#https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#https://www.itread01.com/content/1549051928.html
#https://gist.github.com/econchick/4666413
#https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
#https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
#https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
#https://morioh.com/p/ec5873a4c9f5
#https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
#https://medium.com/cantors-paradise/dijkstras-shortest-path-algorithm-in-python-d955744c7064
#https://github.com/anujdutt9/Python-Data-Structures-and-Algorithms/blob/master/Dijkstras_Algorithm/Dijkstra.py
