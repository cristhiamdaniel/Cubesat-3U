from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
np.random.seed(4)
N = 1000000
#Dos cuadrados paralelos en el origen
l1 = 0.1
w1 = 0.1
z = 0.3
l2 = 0.1
w2 =0.1
l = 0
w = 0
x = w1*np.random.random(N)
y = l1*np.random.random(N)
U = np.random.random(N)
V = np.random.random(N)
theta = 2*np.pi*U
phi = np.arcsin(np.sqrt(V))
counter = 0
for i in range(N):
    r0 = np.array([x[i],y[i],0]) #Punto de donde sale el rayo
    ngx = np.cos(theta[i])*np.sin(phi[i]) #n gorro x
    ngy = np.sin(theta[i])*np.sin(phi[i])
    ngz = np.cos(phi[i])
    if ngz>0:
        S = z/ngz 
        rx = x[i]+ngx*S
        ry = y[i]+ngy*S
        if (w < rx < w+w1) and (l < ry < l+l1):
            counter += 1 # Indica si el rayo cae en el rectangulo se le suma 1
	#plt.plot(rx,ry,'o')
f = counter/N
print("{0:.6f}".format(f))

