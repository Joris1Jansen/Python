class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        path = False
        while queue:
            deVertex = queue.pop(0)
            for adjVertex in self.gdict[deVertex]:
                if adjVertex not in visited:
                    if adjVertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjVertex)
                        queue.append(adjVertex)
        return path


