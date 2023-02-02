"""Utility Functions for Lecture 02"""
from search import DFS


def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)




