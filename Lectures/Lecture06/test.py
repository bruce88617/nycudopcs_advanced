import numpy as np
from scipy.linalg import lu
from numpy.linalg import eig, inv

A = np.array([[.2, .7], [.8, .3]])

# P, L, U = lu(A)
# print(f"P:\n{P}\n")
# print(f"L:\n{L}\n")
# print(f"U:\n{U}\n")

# x = np.array([3, 3, 1])
# print(x.ndim)

# T = np.transpose(A)@A
# print(T)

# P = A@(np.linalg.inv(np.transpose(A)@A))@np.transpose(A)
# print(P)

w, v = eig(A)
print(w)
print(v)

# print(A.shape)
# print(len(A))

