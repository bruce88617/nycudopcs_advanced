import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


def f(x1,x2):
    return (x1**2 + x2 -11)**2 + (x1 + x2**2 -7)**2
    # return -x1**2 * np.exp(-x2**2 + 1) + 1

def loss_fn(x1,x2):
    return (x1**2 + x2 -11)**2 + (x1 + x2**2 -7)**2
    # return -x1**2 * torch.exp(-x2**2 + 1) + 1

def simulator(initial, optimizer, step=100):

    result = [[initial[0].item(), initial[1].item()]]

    for i in range(step):
        optimizer.zero_grad()
        loss = loss_fn(initial[0], initial[1])
        loss.backward()
        optimizer.step()

        result.append([initial[0].item(), initial[1].item()])

    return np.array(result)




