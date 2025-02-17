"""
Testing Functions for Lecture 04
"""


from .basicFuncs import geometricSim
from .utils import runPascal
import numpy as np
import matplotlib.pyplot as plt


def test1(n1=100, n2=1, numExp=100):
    """Simulation of Bias and MSE"""
    result1, result2 = [], []
    theoretical_value = 1-(35/36)**24

    for i in range(numExp):
        result1.append(runPascal(numTrials=n1))
        result2.append(runPascal(numTrials=n2))

    print("n = {:d}:".format(n1))
    print("    Bias = {:.07f}".format(np.mean(result1) - theoretical_value))
    print("    MSE = {:0.7f}".format(np.mean(np.array(result1) - theoretical_value)**2))
    
    print("n = {:d}:".format(n2))
    print("    Bias = {:.07f}".format(np.mean(result2) - theoretical_value))
    print("    MSE = {:0.7f}".format(np.mean(np.array(result2) - theoretical_value)**2))


def test2(p=0.05, numTrials=100, a=0, b=1):
    """Simulation of Point Estimators for Variance"""
    rng = np.random.default_rng()
    for idx, numExp in enumerate((2, 100)):
        sampleVars1, sampleVars2 = [], []

        # n Trials in each experiment
        samples = geometricSim(numTrials=numTrials, p=p)
        # samples = (b-a) * rng.random(numTrials) + a
        sampleMean = np.sum(samples)/numTrials
        sampleVars1.append((1/numTrials) * (np.sum((samples - sampleMean)**2)))
        sampleVars2.append((1/(numTrials-1)) * (np.sum((samples - sampleMean)**2)))
        
        print("Number of Experiment = {:d}:".format(numExp))
        print("    Theoretical value of Variance = {:.07f}".format(
            # (1-p)/p**2
            (b-a)**2 / 12
        ))
        print("    Result of biased estimator of variance = {:.07f}".format(
            np.mean(sampleVars1)
        ))
        print("    Result of unbiased estimator of variance = {:.07f}".format(
            np.mean(sampleVars2)
        ))


