#Import libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Shaft Size - Spherical Coordinates
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=0)

u = np.linspace(0, 2 * np.pi, 120)
v = np.linspace(0, np.pi/2, 60)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='c', alpha = 0.3, linewidth = 0)

# Point Distribution - Lambert 
N = 1000
U = np.random.random(N)
V = np.random.random(N)

theta = 2*np.pi*U
phi = np.arcsin(V)

X = np.zeros(N)
Y = np.zeros(N)
Z = np.zeros(N)

X = np.cos(theta)* np.sin(phi)
Y = np.sin(theta)* np.sin(phi)
Z = np.cos(phi)

# Plot
ax.scatter(X,Y,Z,'o')
plt.figure(2)
plt.plot(X,Y,'o')
plt.axes().set_aspect(1)