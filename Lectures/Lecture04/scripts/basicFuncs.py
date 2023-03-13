"""Basic Functions for Lecture 04"""

import numpy as np

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.
    for x in X:
        tot += (x-mean)**2
    return tot/len(X)

def stdDev(X):
    return variance(X)**0.5


def CV(X):
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')


def gaussDist(x=None, mu=0, sigma=1, N=100):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    if x is None:
        x = np.linspace(mu-5*sigma, mu+5*sigma, N)
    return coeff*np.exp(-((x-mu)**2)/(2*sigma**2))



