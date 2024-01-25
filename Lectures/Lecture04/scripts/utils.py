"""Utility Functions for Lecture 07"""


import random
from .basicFuncs import stdDev, CV, gaussDist, binCoeff


def rollDie():
    return random.choice((1,2,3,4,5,6))


def runPascal(numTrials):
    numWins = 0

    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1==6 and d2==6:
                numWins += 1
                break

    return numWins/numTrials


def estPi(numData):
    inCircle = 0
    for data in range(numData):
        x, y = random.random(), random.random()
        if (x**2 + y**2)**0.5 <= 1:
            inCircle += 1
    return 4*(inCircle/numData)


def getPiEst(numData, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = estPi(numData)
        estimates.append(piGuess)
    std = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)


def throwData(numData):
    count = 0
    for data in range(numData):
        x, y = random.random(), random.random()
        if ((x**2 + y**2)**0.5 <= 1) and \
              (((x-1)**2 + (y-1)**2)**0.5 <= 1):
            count += 1
    return count/numData


def getAreaEst(numData, numTrials):
    estimates = []
    for t in range(numTrials):
        areaGuess = throwData(numData)
        estimates.append(areaGuess)
    std = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)



class poker:
    def __init__(self,):
        self.refresh()
    
    
    def refresh(self):
        suits = ("C", "D", "H", "S")
        self.pool = []
        for i in suits:
            for j in range(1, 14):
                self.pool.append(i+str(j))


    def draw(self):
        card = random.choice(self.pool)
        self.pool.remove(card)
        return card
    

    def getPool(self):
        return self.pool
    

    def removeCards(self, cards = []):
        for card in cards:
            self.pool.remove(card)


def runBJ(numTrials):
    numWins = 0

    pokerPool = poker()
    # remove C5, C13, D10, H4, H9, S1, S7
    pokerPool.removeCards(cards=["C5", "C13", "D10", "H4", "H9", "S1", "S7"])

    


    return numWins/numTrials


