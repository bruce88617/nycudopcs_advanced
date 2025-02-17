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


def factI(n):
    output = 1
    for i in range(n):
        output *= i+1
    return output


def binCoeff(n, k):
    return factI(n)/(factI(k)*factI(n-k))


def gauss2d(**kwargs):
    """Simple version of 2D Gauss function for plotting"""
    x = kwargs.get("x", np.linspace(-1, 1, 101))
    y = kwargs.get("y", np.linspace(-1, 1, 101))
    mean = kwargs.get("mean", (0, 0))
    sigma = kwargs.get("sigma", (1, 1))

    mx, my, sigma_x, sigma_y = mean[0], mean[1], sigma[0], sigma[1]
    xx, yy = np.meshgrid(x, y)
    const = (2 * np.pi * sigma_x * sigma_y)**(-1)

    g2d = np.exp(
        -0.5 * (((xx - mx)/sigma_x)**2 + ((yy - my)/sigma_y)**2)
    ) * const
    
    return g2d


###########################################
###########################################
"""Functions for the figures in lectures"""
import matplotlib.pyplot as plt
import numpy as np


def fig4exercise1():
    """Figure for exercise 1"""
    x = np.linspace(1e-3, 3.5, 101)
    func = lambda x: (1 + np.sin(x) * (np.log(x))**2)**(-1)
    a, b = 0.5, 3
    x2 = np.linspace(a, b, 101)

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")

    ax1 = fig.add_subplot(111)

    ax1.plot(x, func(x), label=r"Function $f(x)$")
    ax1.set_xlim([0, 3.5])
    ax1.set_ylim([0, 2.25])
    ax1.vlines(
        (a, b), 
        ymin = (0, 0), 
        ymax = (func(a), func(b)), 
        colors = 'r', 
        alpha = 0.5,
    )

    ax1.fill_between(x2, y1=np.zeros_like(x2), y2=func(x2), where=None, color='r', alpha=0.1)    
    plt.show()


def fig4multi_variate_MC_integration():
    """Figure for multi-variate MC integration"""
    def gauss2d(**kwargs):
        x = kwargs.get("x", np.linspace(-1, 1, 101))
        y = kwargs.get("y", np.linspace(-1, 1, 101))
        mean = kwargs.get("mean", (0, 0))
        sigma = kwargs.get("sigma", (1, 1))

        mx, my, sigma_x, sigma_y = mean[0], mean[1], sigma[0], sigma[1]
        xx, yy = np.meshgrid(x, y)
        const = (2 * np.pi * sigma_x * sigma_y)**(-1)

        g2d = np.exp(
            -0.5 * (((xx - mx)/sigma_x)**2 + ((yy - my)/sigma_y)**2)
        ) * const
        
        return g2d

    L = 5
    x = np.linspace(-L, L, 101)
    y = np.linspace(-L, L, 101)
    xx ,yy = np.meshgrid(x, y)
    f = gauss2d(mean=(0, 0), sigma=(1, 1), x=x, y=y)

    fig = plt.figure(figsize=(8,4), dpi=100, layout="constrained", facecolor="w")

    ax1 = fig.add_subplot(121)
    # im1 = ax1.imshow(gb1, cmap="jet")
    im1 = ax1.contourf(xx, yy, f, levels=101, cmap="jet")

    ax2 = fig.add_subplot(122, projection="3d")
    im2 = ax2.plot_surface(xx, yy, f, cmap="jet")

    plt.show()


def fig4exercise2():
    """Figure for exercise 2"""
    def gabor(sigma, theta, gamma, **kwargs):
        x = kwargs.get("x", np.linspace(-1, 1, 101))
        y = kwargs.get("y", np.linspace(-1, 1, 101))

        sigma_x = sigma
        sigma_y = float(sigma) / gamma
        xx, yy = np.meshgrid(x, y)

        # Rotation
        x_theta = xx * np.cos(theta) + yy * np.sin(theta)
        y_theta = -xx * np.sin(theta) + yy * np.cos(theta)

        gb = np.exp(
            -0.5 * (x_theta**2 / sigma_x**2 + y_theta**2 / sigma_y**2)
        ) * np.cos(2 * np.pi * x_theta)
        
        return gb

    L = 1
    x = np.linspace(-L, L, 101)
    y = np.linspace(-L, L, 101)
    xx ,yy = np.meshgrid(x, y)
    gb1 = gabor(sigma=0.4, theta=np.pi/4, gamma=2, x=x, y=y)

    fig = plt.figure(figsize=(8,4), dpi=100, layout="constrained", facecolor="w")

    ax1 = fig.add_subplot(121)
    # im1 = ax1.imshow(gb1, cmap="jet")
    im1 = ax1.contourf(xx, yy, gb1, levels=101, cmap="jet")

    ax2 = fig.add_subplot(122, projection="3d")
    im2 = ax2.plot_surface(xx, yy, gb1, cmap="jet")

    plt.show()


def uniform(x, a, b):
    const = 1/(b-a)
    y = np.zeros_like(x)
    y[x>=a and x<b] = const
    return y



