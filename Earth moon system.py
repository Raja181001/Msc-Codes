from matplotlib.pyplot import *
from numpy import *

def circle(r,th,ph,x,y,z):
    x1 = r * sin(th) * cos(ph) + x
    y1 = r * sin(th) * sin(ph) + y
    z1 = r * cos(th) + z
    return x1,y1,z1

def ellipse(a,b,th):
    x = a * cos(th)
    y = b * sin(th)
    return x,y

r = [6.371,1.7374,384.400,383.800]
c = sqrt(square(r[2])-square(r[3]))
th = linspace(0,2*pi,10000)
orbit = ellipse(r[2],r[3],th)
ph = linspace(0,pi,10000)
th , ph = meshgrid(th,ph)
earth = circle(r[0],th,ph,c,0,0)

moon = circle(r[1],th,ph,r[2],0,0)
figure(figsize=[40,40])
ax = axes(projection = '3d')
ax.plot_surface(earth[0],earth[1],earth[2],color='blue')
ax.plot_surface(moon[0],moon[1],moon[2],color='blue')
ax.plot(orbit[0],orbit[1],color='red',linewidth='1')
ax.axis('equal')
ax.axis('off')
ax.grid(False)

show()