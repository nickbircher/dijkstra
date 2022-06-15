class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.visited = False
        self.prev = None  # prev node
        self.dist = 0
        self.path = []  # path arr

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __repr__(self):
        return str(self.id)

    def getConnections(self):
        return list(self.connectedTo.keys())

    def getId(self):
        return self.id

    def set_visited(self):
        self.visited = True

    def is_visited(self):
        return self.visited

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def set_distance(self, dist):
        self.dist = dist

    def get_distance(self):
        return self.dist

    def previous(self, prev):
        self.prev = prev


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def addBiEdge(self, f, t, weight=1):
        self.addEdge(f, t, weight)
        self.addEdge(t, f, weight)

    def getVertices(self):
        return self.vertList.values()

    def __iter__(self):
        return iter(self.vertList.values())


def shortest_path(start, graph):
    """shortest path to every node, returns list [target, [path], cost]"""
    """q.pop(0) for dequeue, q.append(item) for enqueue"""
    q = []
    graph = graph.getVertices()
    for v in graph:
        v.set_distance(1000)
    q.append(start)
    start.set_distance(0)
    """while nodes left in queue"""
    while len(q) > 0:
        node = q.pop(0)
        node.set_visited()
        """setting minimum distances for each node"""
        for nbr in node.getConnections():
            """if new dist < old min dist, replace dist"""
            new_dist = node.get_distance() + node.getWeight(nbr)
            if new_dist < nbr.get_distance():
                nbr.set_distance(new_dist)
                """set prev for path"""
                nbr.prev = node
                if not nbr.is_visited():
                    q.append(nbr)

    """building path by iterating from vertex back to start node using prev node"""
    for vertex in graph:
        temp = vertex
        path = []
        """while temp is not an empty node and is not start node"""
        while temp is not None and temp.getId() != start.getId():
            path.insert(0, temp)
            temp = temp.prev
        path.insert(0, start)
        vertex.path = path

    res = []
    """building the result array in order: goal, path, cost"""
    for vertex in graph:
        res.append([vertex, vertex.path, vertex.get_distance()])

    return res
  
