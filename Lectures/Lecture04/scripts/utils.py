"""Utility Functions for Lecture 04"""

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollSim(numTimes=5, seed=False):
    if seed:
        random.seed(0)
    result = ""
    for t in range(numTimes):
        result += str(rollDie())
    return result


