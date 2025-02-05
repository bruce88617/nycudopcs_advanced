from func import f, loss_fn
import torch
import torch.optim as optim
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

torch.manual_seed(0)

x1 = torch.tensor([torch.randn(1)], requires_grad=True)
x2 = torch.tensor([torch.randn(1)], requires_grad=True)

lr = 1e-3
# # SGD
# optimizer = optim.SGD([x1,x2], lr=lr)
# Momentum
# optimizer = optim.SGD([x1,x2], lr=lr, momentum=0.9)
# Adam
optimizer = optim.Adam([x1,x2], lr=lr)

step = 30
result = [[x1.item(),x2.item()]]

for i in range(step):
    
    
    loss = loss_fn(x1,x2)
    loss.backward()
    
    optimizer.step()
    optimizer.zero_grad()
    
    # print([x1, x2])
    result.append([x1.item(), x2.item()])

result = np.array(result)

# # Save the result
# np.save("./Lectures/Lecture08/data/adam{:.04f}.npy".format(lr), result)

# Plot the resul
L = 5
x = np.linspace(-L, L, 501).reshape(1, -1)
y = np.linspace(-L, L, 501).reshape(-1, 1)
X, Y = np.meshgrid(x,y)
Z = f(X, Y)

fig = plt.figure(figsize=(8, 6))

ax2 = fig.add_subplot(111)
im1 = ax2.contourf(X,Y,np.log(Z), cmap=mpl.cm.terrain, levels=10, extent=[-L, L, -L, L])
im2 = ax2.contour(X,Y,np.log(Z), cmap=mpl.cm.hot, levels=10, extent=[-L, L, -L, L])
ax2.clabel(im2, inline=True, fontsize=8)

ax2.plot(result[:,0], result[:,1], "r")
ax2.set(xlim=[-L,L], ylim=[-L,L], xlabel="x", ylabel="y")

plt.show()

