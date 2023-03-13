"""Testing Functions for Lecture 04"""

from .utils import rollSim, flipSim, flip, makePlot, labelPlot
from .basicFuncs import stdDev, CV, gaussDist, binCoeff
import matplotlib.pyplot as plt
import numpy as np


def test1(numRollsPerTrial=5, numTrials=5, seed=False):
    print("Rolling a fair dice {} times".format(numRollsPerTrial))
    for t in range(numTrials):
        print("    {} trials: {}".format(t+1, rollSim(numTimes=numRollsPerTrial, seed=seed)))


def test2(numFlipsPerTrial=10, numTrials=10, numExps=5):
    print("Flipping a fair coin {} times".format(numFlipsPerTrial))
    for e in range(numExps):
        _, m, _ = flipSim(numFlipsPerTrial=numFlipsPerTrial, numTrials=numTrials)
        print("    {} Experiment: Mean = {}".format(e+1, m))


def test3(numFlipsPerTrial=10, numTrials=100):
    fracHeads = []
    for t in range(numTrials):
        numHeads, _ = flip(numFlipsPerTrial)
        fracHeads.append(numHeads/numFlipsPerTrial)

    extremes, nextTrials, avgs = [], [], []
    for i in range(len(fracHeads)-1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
            avgs.append((fracHeads[i]+fracHeads[i+1])/2)

    fig = plt.figure(1, dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(range(len(extremes)), extremes, 'ko', label="Extreme")
    ax.plot(range(len(nextTrials)), nextTrials, 'k^', label="Next Trial")
    ax.plot(range(len(avgs)), avgs, 'r.', label="(Extreme+Next Trial)/2")
    ax.axhline(0.5)
    ax.set_ylim([0,1])
    ax.set_xlim([-1, len(extremes)+1])
    ax.set_xlabel("Extreme Example and Next Trial")
    ax.set_ylabel("Fraction Heads")
    ax.set_title("Regression to the Mean")
    ax.legend(loc='best')

    plt.show()


def test4(minExp=4, maxExp=20):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)

    for numFlips in xAxis:
        numHeads, numTails = flip(numFlips)

        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
            # diffs.append((numHeads-numTails))
        except ZeroDivisionError:
            continue
    
    fig = plt.figure(figsize=(8,4), dpi=100, layout="constrained")
    ax1 = fig.add_subplot(121)
    ax1.plot(xAxis, diffs, 'ko')
    ax1.plot(xAxis, diffs, 'k')
    ax1.set_xscale('log')
    ax1.set_xlabel("Number of Flips")
    ax1.set_ylabel("Abs(#Heads - #Tails)")
    ax1.set_title("Difference Between Heads and Tails")
    ax2 = fig.add_subplot(122)
    ax2.set_title("Heads/Tails Ratios")
    ax2.set_xlabel("Number of Flips")
    ax2.set_ylabel("#Heads/#Tails")
    ax2.set_xscale('log')
    ax2.plot(xAxis, ratios, 'ko')
    ax2.plot(xAxis, ratios, 'k')

    plt.show()


def test5(minExp=4, maxExp=20, numTrials=20):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = flip(numFlips)
            ratios.append(numHeads/numTails)
            # diffs.append(abs(numHeads-numTails))
            diffs.append((numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        
    fig = plt.figure(figsize=(8,8), dpi=100, layout="constrained")
    ax1 = fig.add_subplot(221)
    makePlot(ax1, xVals=xAxis, yVals=ratiosMeans, title="Mean Heads/Tails Ratios ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Mean Heads/Tails", style='ko', logX=True)
    ax2 = fig.add_subplot(222)
    makePlot(ax2, xVals=xAxis, yVals=ratiosSDs, title="SD Heads/Tails Ratios ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Standard Deviation", style='ko', logX=True, logY=True)
    ax3 = fig.add_subplot(223)
    makePlot(ax3, xVals=xAxis, yVals=diffsMeans, title="Mean Differences ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Mean Differences", style='ko', logX=True, logY=False)
    ax4 = fig.add_subplot(224)
    makePlot(ax4, xVals=xAxis, yVals=diffsSDs, title="SD Differences ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Standard Deviation", style='ko', logX=True, logY=True)
    
    plt.show()


def test6(minExp=4, maxExp=20, numTrials=20):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis, ratiosCVs, diffsCVs = [], [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = flip(numFlips)
            ratios.append(numHeads/numTails)
            # diffs.append(abs(numHeads-numTails))
            diffs.append((numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
        
    fig1 = plt.figure(figsize=(10,4), dpi=100, layout="constrained")
    ax1 = fig1.add_subplot(121)
    makePlot(ax1, xVals=xAxis, yVals=ratiosMeans, title="Mean Heads/Tails Ratios ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Mean Heads/Tails", style='ko', logX=True)
    ax2 = fig1.add_subplot(122)
    makePlot(ax2, xVals=xAxis, yVals=ratiosSDs, title="SD Heads/Tails Ratios ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Standard Deviation", style='ko', logX=True, logY=True)
    
    fig2 = plt.figure(figsize=(10,4), dpi=100, layout="constrained")
    ax1 = fig2.add_subplot(121)
    makePlot(ax1, xVals=xAxis, yVals=diffsMeans, title="Mean Differences ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Mean Differences", style='ko', logX=True, logY=False)
    ax2 = fig2.add_subplot(122)
    makePlot(ax2, xVals=xAxis, yVals=diffsSDs, title="SD Differences ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Standard Deviation", style='ko', logX=True, logY=True)
    
    fig3 = plt.figure(figsize=(10,4), dpi=100, layout="constrained")
    ax1 = fig3.add_subplot(121)
    makePlot(ax1, xVals=xAxis, yVals=ratiosCVs, title="Coeff. of Var. Heads/Tails Ratios ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Coeff. of Var.", style='ko', logX=True, logY=True)
    ax2 = fig3.add_subplot(122)
    makePlot(ax2, xVals=xAxis, yVals=diffsCVs, title="Coeff. of Var. Difference ({} Trials)".format(numTrials), 
             xLabel="Number of Flips", yLabel="Coeff. of Var.", style='ko', logX=True)
    
    plt.show()


def test7(numFlips1=100, numFlips2=1000, numTrials=10000):
    v1, m1, s1 = flipSim(numFlipsPerTrial=numFlips1, numTrials=numTrials)
    v2, m2, s2 = flipSim(numFlipsPerTrial=numFlips2, numTrials=numTrials)
    
    fig = plt.figure(figsize=(10,4), dpi=100, layout="constrained")
    ax1 = fig.add_subplot(121)
    ax1.hist(v1, bins=20)
    xmin, xmax = ax1.get_xlim()
    labelPlot(ax1, numFlips=numFlips1, numTrials=numTrials, mean=m1, std=s1)
    ax2 = fig.add_subplot(122)
    ax2.hist(v2, bins=20)
    ax2.set_xlim([xmin, xmax])
    labelPlot(ax2, numFlips=numFlips2, numTrials=numTrials, mean=m2, std=s2)

    plt.show()


def test8(x=None, mu=0, sigma=1, N=100):
    if x is None:
        x = np.linspace(mu-5*sigma, mu+5*sigma, N)
    y = gaussDist(x=x, mu=0, sigma=1)

    xfill1 = np.linspace(-sigma,sigma,20)
    yfill1 = gaussDist(x=xfill1)
    xfill2 = np.linspace(-2*sigma,-sigma,20)
    yfill2 = gaussDist(x=xfill2)
    xfill3 = np.linspace(sigma,2*sigma,20)
    yfill3 = gaussDist(x=xfill3)
    xfill4 = np.linspace(2*sigma,3*sigma,20)
    yfill4 = gaussDist(x=xfill4)
    xfill5 = np.linspace(-3*sigma,-2*sigma,20)
    yfill5 = gaussDist(x=xfill5)

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'k', label="Normal distribution")
    ax.fill_between(xfill1, y1=yfill1, y2=0, where=None, color='g', alpha=0.2)
    ax.fill_between(xfill2, y1=yfill2, y2=0, where=None, color='b', alpha=0.2)
    ax.fill_between(xfill3, y1=yfill3, y2=0, where=None, color='b', alpha=0.2)
    ax.fill_between(xfill4, y1=yfill4, y2=0, where=None, color='r', alpha=0.2)
    ax.fill_between(xfill5, y1=yfill5, y2=0, where=None, color='r', alpha=0.2)
    ax.set_xlim(-4,4)
    ax.set_ylim(0, np.max(y)*1.1)
    ax.annotate("~68.27%", size="x-large", xycoords="axes fraction", xy=(0.4,0.5))
    ax.annotate("~95.45%", size="x-large", xycoords="axes fraction", xy=(0.4,0.12))
    ax.annotate("~99.73%", size="x-large", xycoords="axes fraction", xy=(0.4,0.01))
    ax.hlines(np.max(y)*0.52, -sigma, sigma, 'g', alpha=0.5)
    ax.hlines(np.max(y)*0.12, -2*sigma, 2*sigma, 'b', alpha=0.5)
    ax.hlines(np.max(y)*0.01, -3*sigma, 3*sigma, 'r', alpha=0.5)
    ax.legend(loc='best')
    ax.set_title("Normal Distribution, Mean = {} and STD = {}".format(mu, sigma))

    plt.show()


def test9(minExp=3, maxExp=10, numTrials=100):
    means, stds, xVals = [], [], []

    for exp in range(minExp, maxExp+1):
        xVals.append(2**exp)
        _, mean, std = flipSim(2**exp, numTrials)
        means.append(mean)
        stds.append(std)

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained")
    ax1 = fig.add_subplot(111)
    ax1.errorbar(xVals, means, yerr=1.96*np.array(stds))
    ax1.set_xscale("log")
    ax1.set_xlabel("Number of flips per trial")
    ax1.set_ylabel("Fraction of heads & 95% confidence")
    ax1.set_title("Mean Fraction of Heads ({})".format(numTrials))
    
    plt.show()


def test10(minExp=2, maxExp=100, p=1/6, times=2):
    xVals, results = [], []
    for i in range(minExp, maxExp+1):
        prob = binCoeff(i, times) * (p)**times * (1-p)**(i-times)
        xVals.append(i)
        results.append(prob)
    
    fig = plt.figure(dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(xVals, results)
    ax.set_title("Probability of Rolling Two 3's")
    ax.set_xlabel("Number of rolls")
    ax.set_ylabel("Probability")
    ax.set_xlim(xVals[0], xVals[-1])
    ax.set_ylim(0, np.max(results)*1.1)

    plt.show()








