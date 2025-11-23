class Graph:
    def __init__(self,vertices):
        self.graph = []

        for i in range(vertices):
            self.graph.append([])
            for j in range(vertices):
                self.graph[i].append(0)
    
    def add_edge(self, u, v):
        self.graph[u][v] = 1

g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
print(g.graph)
