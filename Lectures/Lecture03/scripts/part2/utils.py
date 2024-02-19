"""
Utility Functions for Lecture 03

Part II: Stochastic Programs
"""


import random
import scipy
from .basicFuncs import stdDev, gaussDist


def rollDie():
    return random.choice((1,2,3,4,5,6))


def rollSim(numTimes=5, seed=False):
    if seed:
        random.seed(0)
    result = ""
    for t in range(numTimes):
        result += str(rollDie())
    return result


def flipCoin():
    return random.choice(("H", "T"))


def flip(numFlips):
    numHeads = 0
    for i in range(numFlips):
        if flipCoin() == "H":
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        numHeads, _ = flip(numFlipsPerTrial)
        fracHeads.append(numHeads/numFlipsPerTrial)
    mean = sum(fracHeads)/len(fracHeads)
    std = stdDev(fracHeads)
    return (fracHeads, mean, std)


def makePlot(ax, xVals, yVals, title, xLabel, yLabel, style, logX=False, logY=False):
    ax.plot(xVals, yVals, style)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    if logX:
        ax.set_xscale("log")
    if logY:
        ax.set_yscale("log")


def labelPlot(ax, numFlips, numTrials, mean, std):
    ax.set_title("{} trials of {} flips each".format(numTrials, numFlips))
    ax.set_xlabel("Fraction of Heads")
    ax.set_ylabel("Number of Trials")
    ax.annotate("Mean = {:.04f}\nSTD = {:.04f}".format(mean, std), size="x-large", xycoords="axes fraction", xy=(0.6,0.8))


def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10,10)
        sigma = random.randint(1,10)
        print("Normal distribution with (\u03BC, \u03C3) = ({}, {})".format(mu, sigma))
        for numStd in (1, 2, 3):
            area = scipy.integrate.quad(gaussDist, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print("    Area within {} std = {:.04f}".format(numStd, area))







