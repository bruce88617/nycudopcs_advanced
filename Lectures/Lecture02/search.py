"""Search Algorithms for Lecture 02"""


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    
    if toPrint:
        print("Current DFS path:", printPath(path))

    if start == end:
        return path
    
    for node in graph.childrenOf(start):
        # avoid cycles
        if node not in path: 
            
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                
                if newPath != None:
                    shortest = newPath
                    # print("Current shortest path:", printPath(shortest))
    
    return shortest


def printPath(path):
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result += "->"
    return result



