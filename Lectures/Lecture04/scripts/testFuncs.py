"""Testing Functions for Lecture 07"""

from .utils import runPascal, getPiEst, getAreaEst, getIntegralEst, getIntegralEst2d, getBattingData, makeHist, sampleData, sampleDataFromUniform
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def test1():
    print("Run Simulation of Pascal's Game")

    p = []
    xAxis = np.geomspace(1, 2**19, 20, dtype=np.int64)

    for numTrials in xAxis:
        p.append(runPascal(numTrials))

    print("    Probability of winning = {:.04f}".format(p[-1]))

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.plot(
        xAxis,
        p, 
        'ko', 
        label="Experimental results\nEstimated probability = {:.04f}".format(p[-1]),
    )
    ax1.set_title("Simulation of Pascal's Problem")
    ax1.set_xlabel("Number of Trials")
    ax1.set_ylabel("Winning Probability")
    ax1.set_xscale("log")
    ax1.set_ylim([0, 1])

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        1-(35/36)**24, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Theoretical value = {:.04f}".format(1-(35/36)**24)
    )
    ax1.legend(loc="best")
    
    plt.show()

    
def test2(numTrials=100, numData=2**15, toPrint=False):

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getPiEst(numData=val, numTrials=numTrials)
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.06f}, STD = {:.06f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.06f}".format(yEsts[-1]),
    )
    ax1.set_title(r"Simulation of $\pi$ Estimation")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        np.pi, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Theoretical value = {:.06f}".format(np.pi)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test3(numTrials=100, numData=2**15, toPrint=False):

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getAreaEst(numData=val, numTrials=numTrials)
        
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
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.06f}".format(yEsts[-1])
    )
    ax1.set_title("Simulation of Area Estimation")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        np.pi/2 - 1, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Analytical value = {:.06f}".format(np.pi/2 - 1)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test4(numTrials=100, numData=2**15, **kwargs):
    a = kwargs.get("a", 1.2)
    b = kwargs.get("b", 3.5)
    func = kwargs.get("func", lambda x: 0.5*x)
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
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.05f}".format(yEsts[-1]),
    )
    ax1.set_title("Simulation of Monte Carlo Integration")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        2.7025, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Analytical value = {:.05f}".format(2.7025)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test5(numTrials=100, numData=2**15, **kwargs):
    a = kwargs.get("a", (-1, -1))
    b = kwargs.get("b", (1, 1))
    toPrint = kwargs.get("toPrint", True)

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getIntegralEst2d(
            numData=val, 
            numTrials=numTrials, 
            a=a, 
            b=b, 
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

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        1 - np.exp(-0.5),
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "{:.05f}".format(1 - np.exp(-0.5))
    )

    ax1.legend(loc="best")
    
    plt.show()


def test6(numSamples=(20, 100, 200)):
    batting2023 = getBattingData("./data/data_batting2023.csv",)
    ba_2023 = batting2023["BA"].to_numpy()
    # makeHist(
    #     ba_2023, 
    #     title="2023 MLB Season",
    #     xlabel="Batting Average",
    #     ylabel="Number of Batters",
    # )

    for num in numSamples:
        sampleData(ba_2023, numSamples=num)


def test7(numSamples=40, numTrials=1000):
    tightMeans, wideMeans = sampleDataFromUniform(numTrials=numTrials, numSamples=numSamples)

    fig1 = plt.figure(1, figsize=(10,4), dpi=100, layout="constrained")

    ax1 = fig1.add_subplot(121)
    ax1.plot(wideMeans, 'g*', label='STD = {:.02f}'.format(np.sqrt(200**2/12)))
    ax1.plot(tightMeans, 'bo', label='STD = {:.02f}'.format(np.sqrt(6**2/12)))
    ax1.set_xlabel('Sample Number')
    ax1.set_ylabel('Sample Mean')
    ax1.set_title('Means of Sample Size {}'.format(numSamples))
    ax1.legend()

    ax2 = fig1.add_subplot(122)
    ax2.hist(wideMeans, bins=20, color='g', alpha=0.2, label='STD = {:.02f}'.format(np.sqrt(200**2/12)))
    ax2.hist(tightMeans, bins=20, color='b', alpha=0.2, label='STD = {:.02f}'.format(np.sqrt(6**2/12)))
    ax2.set_title('Distribution of Sample Means')
    ax2.set_xlabel('Sample Mean')
    ax2.set_ylabel('Frequency of Occurence')
    ax2.legend()

    plt.show()


def test8(numSamples=(10, 50, 100,)):
    for num in numSamples:
        tightMeans, wideMeans = sampleDataFromUniform(1000, numSamples=num)
        tMean, tVar = np.mean(tightMeans), np.var(tightMeans)
        wMean, wVar = np.mean(wideMeans), np.var(wideMeans)
        tVar_truth, wVar_truth = 6**2/12, 200**2/12
        print("Result of simulation, number of samples = {}:".format(num))
        print("-"*60)
        print("Mean of tight distribution (s, p) = ({:.02f}, {:.02f})".format(tMean, 0))
        print("Variance of tight distribution (s, p) = ({:.02f}, {:.02f})".format(tVar, tVar_truth))
        print("Mean of wide distribution (s, p) = ({:.02f}, {:.02f})".format(wMean, 0))
        print("Variance of wide distribution (s, p) = ({:.02f}, {:.02f})".format(wVar, wVar_truth))
        print("="*60)


# CLT
def test9(numSamples=(10, 50, 100,)):
    for num in numSamples:
        tightMeans, wideMeans = sampleDataFromUniform(1000, numSamples=num)
        tMean, tSTD = np.mean(tightMeans), np.std(tightMeans)
        wMean, wSTD = np.mean(wideMeans), np.std(wideMeans)
        tSTD_truth, wSTD_truth = np.sqrt(6**2/12), np.sqrt(200**2/12)
        print("Result of simulation, number of samples = {}:".format(num))
        print("-"*60)
        print("Mean of tight distribution (s, p) = ({:.02f}, {:.02f})".format(tMean, 0))
        print("STD of tight distribution (s, p) = ({:.02f}, {:.02f})".format(tSTD, tSTD_truth))
        print("    The mean of population is {:.02f}±{:.02f} with 95% confidence.".format(tMean, 1.96*tSTD))
        print("Mean of wide distribution (s, p) = ({:.02f}, {:.02f})".format(wMean, 0))
        print("STD of wide distribution (s, p) = ({:.02f}, {:.02f})".format(wSTD, wSTD_truth))
        print("    The mean of population is {:.02f}±{:.02f} with 95% confidence.".format(wMean, 1.96*wSTD))
        print("="*60)

