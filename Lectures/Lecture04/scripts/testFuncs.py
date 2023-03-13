"""Testing Functions for Lecture 04"""

from .utils import rollSim



def test1(numTimes=5, numTrials=5, seed=False):
    print("Rolling a fair dice {} times".format(numTimes))
    for t in range(numTrials):
        print("    {} trials: {}".format(t, rollSim(numTimes=numTimes, seed=seed)))






