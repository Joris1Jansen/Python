class Graph:

    def __init__(self, gDict=None):
        if gDict is None:
            gDict = {}
        else:
            self.gDict = gDict
    
    def addEdge(self, vertex, edge):
        self.gDict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            DequeueVertex = queue.pop(0)
            print(DequeueVertex)
            for adjacentVertex in self.gDict[DequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gDict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}

newGraph = Graph(customDict)
print(newGraph.gDict)

newGraph.addEdge("e", "c")
print(newGraph.gDict)

newGraph.bfs("a")
print('------')
newGraph.dfs("a")