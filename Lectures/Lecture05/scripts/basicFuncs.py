"""Basic Functions for Lecture 05"""

import numpy as np
import random
from scipy.integrate import quad

def createData4example():
    treatmeantDist = (173., 4.)
    controlDist = (170., 5.5)
    sampleSize = 100

    treatmeantHeights, controlHeights = [], []

    for s in range(sampleSize):
        treatmeantHeights.append(random.gauss(treatmeantDist[0], treatmeantDist[1]))
        controlHeights.append(random.gauss(controlDist[0], controlDist[1]))

    treatmeantHeights = np.array(treatmeantHeights)
    controlHeights = np.array(controlHeights)
    
    return treatmeantHeights, controlHeights


def gaussDist(x=None, mu=0, sigma=1, N=100):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    if x is None:
        x = np.linspace(mu-5*sigma, mu+5*sigma, N)
    return coeff*np.exp(-((x-mu)**2)/(2*sigma**2))


def calProb(x, mu=0, sigma=1):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    func = lambda x: coeff*np.exp(-((x-mu)**2)/(2*sigma**2))
    prob = quad(func, 0, x)[0]
    return (0.5 - prob)*2





###########################################
###########################################
"""Functions for the figures in lectures"""
import matplotlib.pyplot as plt



zValue = (mTreat - 170) / (5.5/np.sqrt(100))
pValue = calProb(zValue)

print("z-value = {:.03f}".format(zValue))
print("Probability = {:.05f}".format(pValue))

x = np.linspace(-7, 7, 101)
x2 = np.linspace(-zValue, zValue, 101)

fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
ax1 = fig.add_subplot(111)
ax1.plot(x, gaussDist(x), 'b', label="Mean = {}\nSTD = {}".format(0, 1))
ax1.vlines([-zValue, zValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="Z-value = {:.03f}".format(zValue))
ax1.plot(zValue, pValue+0.01, 'rv', markersize=5, label="Probability = {:.05f}".format(pValue))
ax1.fill_between(x2, y1=gaussDist(x2), y2=0, color='g', alpha=0.2)
ax1.set_title("Normalized Distribution")
ax1.set_xlabel("Z")
ax1.set_ylabel("Probability")
ax1.set_xlim([-7, 7])
ax1.set_ylim([0, 0.5])
ax1.legend(loc=2)    # upper left
    
plt.show()