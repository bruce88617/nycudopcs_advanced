from scripts.utils import buildGraph1, buildGraph2, buildGraph3, shortestPath, printPath
from scripts.search import DFS, BFS

def test1():
    g = buildGraph1()
    start = g.getNode(0)
    end = g.getNode(5)
    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))

def test2():
    g = buildGraph2()
    start = g.getNode(0)
    end = g.getNode(-1)
    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))

def test3():
    g = buildGraph1()
    start = g.getNode(0)
    end = g.getNode(5)
    found = DFS(g, start, end, [], toPrint=False)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))

def test4():
    g = buildGraph2()
    start = g.getNode(0)
    end = g.getNode(-1)
    found = DFS(g, start, end, [], toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))

def test5():
    g = buildGraph3()
    start = g.getNode(0)
    end = g.getNode(-1)
    found = DFS(g, start, end, [], toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))




