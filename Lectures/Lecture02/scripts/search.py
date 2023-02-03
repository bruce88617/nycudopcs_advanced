"""Search Algorithms for Lecture 02"""


def DFS(graph, start, end, path, toPrint=False, foundPath=[]):
    path = path + [start]
    
    if toPrint:
        print("Current DFS path:", printPath(path))
    
    if start == end:
        return foundPath.append(printPath(path))
    
    for node in graph.childrenOf(start):
        if node not in path:
            DFS(graph, node, end, path, toPrint, foundPath=foundPath)
    
    return foundPath


def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    foundPath = []

    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]

        if toPrint:
            print("Current BFS path:", printPath(tmpPath))

        if lastNode == end:
            foundPath.append(printPath(tmpPath))
        
        for nextNode in graph.childrenOf(lastNode):
            
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
            
    return foundPath


def printPath(path):
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result += "->"
    return result



