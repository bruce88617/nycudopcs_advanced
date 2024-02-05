"""
Solution of exercises in Lecture 04
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import quad
from .basicFuncs import stdDev
from .utils import getIntegralEst


def exercise1(numTrials=100, numData=2**15, **kwargs):
    a = kwargs.get("a", 0.5)
    b = kwargs.get("b", 3.)
    func = kwargs.get("func", lambda x: (1 + np.sin(x) * (np.log(x))**2)**(-1))
    toPrint = kwargs.get("toPrint", True)

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getIntegralEst(
            numData=val, 
            numTrials=numTrials, 
            a=a, 
            b=b, 
            func=func
        )
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.05f}, STD = {:.05f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(xAxis, yEsts, 'ko', label="Estimations")
    ax1.set_title("Exercise 1")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    scipyResult = quad(func=func, a=a, b=b)
    ax1.hlines(
        scipyResult[0],
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "{:.05f}".format(scipyResult[0])
    )
    ax1.legend(loc="best")
    
    plt.show()


def exercise2(numTrials=100, numData=2**15, **kwargs):
    def est4exercise2(numData, numTrials, a, b, func):
        estimates = []
        for t in range(numTrials):
            integralGuess = mcFunc4exercise2(numData, a=a, b=b, func=func)
            estimates.append(integralGuess)
        std = stdDev(estimates)
        curEst = sum(estimates)/len(estimates)
        return (curEst, std)

    def mcFunc4exercise2(numData, a, b, func):
        I = 0.
        a1, a2, b1, b2 = a[0], a[1], b[0], b[1]
        for data in range(numData):
            x = (b1-a1)*random.random() + a1
            y = (b2-a2)*random.random() + a2
            if abs(x-0.3)/2 + abs(y-0.3) <= 0.25:
                I += func(x, y)
        return 1*0.5*0.5*I/numData
    
    def gabor(x, y):
        """Simple version Gabor function for Monte Carlo"""
        sigma, theta, gamma = 0.4, np.pi/4, 2
        sigma_x = sigma
        sigma_y = sigma / gamma
        # Rotation
        x_theta = x * np.cos(theta) + y * np.sin(theta)
        y_theta = -x * np.sin(theta) + y * np.cos(theta)
        gb = np.exp(
            -0.5 * (x_theta**2 / sigma_x**2 + y_theta**2 / sigma_y**2)
        ) * np.cos(2 * np.pi * x_theta)
        return gb

    a = kwargs.get("a", (-0.2, 0.05))
    b = kwargs.get("b", (0.8, 0.55))
    func = kwargs.get("func", gabor)
    toPrint = kwargs.get("toPrint", True)

    xVals, yEsts, yStds= [], [], []
    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = est4exercise2(
            numData=val, 
            numTrials=numTrials, 
            a=a, 
            b=b, 
            func=func,
        )
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.05f}, STD = {:.05f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(xAxis, yEsts, 'ko', label="Estimations")
    ax1.set_title("Simulation of 2D Monte Carlo Integration")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")
    ax1.legend(loc="best")
    
    plt.show()



