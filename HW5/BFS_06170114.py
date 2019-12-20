from collections import defaultdict

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self, u, v): 
        self.graph[u].append(v) 
        
    def BFS(self, s):
        queue, visited = [], []
        queue.append(s)
        visited.append(s)
        a = queue
        while queue:
            for i in self.graph[queue.pop()]:
                c = visited
                if i in visited:
                    continue
                else:
                    visited.append(i)
                    queue.append(i)
        return visited
        
    def DFS(self, s):
        queue, visited = [], []
        visited.append(s)
        b = queue
        for i in self.graph[s]:
            queue.append(i)
        while len(queue)>0: 
            a=queue.pop() 
            visited.append(a)
            c = visited
            for j in self.graph[a]:
                if j not in visited: 
                    if j not in queue: 
                        queue.append(j)
        return visited

#參考資料
#https://www.itread01.com/content/1542363063.html
#https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
#https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html

