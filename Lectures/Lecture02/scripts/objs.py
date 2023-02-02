"""Objects for Lecture 02"""


class Node:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return "{} -> {}".format(self.src, self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.):
        super(self, Edge).__init__(src, dest)
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return "{} -({})-> {}".format(self.src, self.weight, self.dest)

class Digraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
    
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Node already exists, idiot")
        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node is not in graph, idiot")
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += "{} -> {}\n".format(src.getName(), dest.getName())
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

