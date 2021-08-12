# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:50:41 2020

@author: Daniel
"""

from numpy import random, cos, sin, sqrt, pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def rand_sphere(n):
     """n points distributed evenly on the surface of a unit sphere""" 
     z = 2 * random.rand(n) - 1   # uniform in -1, 1
     theta = 2 * pi * random.rand(n)   # uniform in 0, 2*pi
     x = sqrt(1 - z**2) * cos(theta)
     y = sqrt(1 - z**2) * sin(theta)
     return x, y, z

x, y, z = rand_sphere(1000)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()