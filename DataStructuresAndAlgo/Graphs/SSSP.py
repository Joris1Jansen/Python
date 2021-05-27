class Graph:

    def __init__(self, gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict
    
    def BFS(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gDict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

customDict = {
    "a" : ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"],
}

NewGraph = Graph(customDict)
print(NewGraph.BFS("a", "g"))
