# date: 6/29/2021
# goal: to make a 3-D lorenz strange attractor plot

import matplotlib.pyplot as plt

from rk4thOrderXYZ import rungekutta

plt.xlim(0,5)
plt.ylim(0,5)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


x, y, z, t, n = rungekutta(0, 40, 1, 1, 1, 0.001)

ax.plot(x, y, z, c='blue')

# optional code if you want a dot to trace out the path of the system
#for i in range(0,n,20):
    #dot = ax.scatter3D(x[i], y[i], z[i], c = 'black')
    #plt.pause(0.01)
    #dot.remove()

plt.show()