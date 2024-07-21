from numpy import *
from matplotlib.pyplot import *
from scipy.constants import *
k = 1/(4*pi*epsilon_0)
x = -1
y = 10
q1 = e
q2 = e
t = 0.01
x0 = 2
y0 = 5
m = electron_mass
x1 = []
y1 = []
x00 = []
y00 = []
t1 = 0.01
v0x = 10
v0y = -30
v = -1
v1 = -1
i = 0
while t1 < 0.5:

  r = sqrt((x-x0)**2 + (y-y0)**2)
  ax = (k*q1*q2*(x-x0))/(pow(r,3)*m)
  ay = (k*q1*q2*(y-y0))/(pow(r,3)*m)
  vx = v0x + ax*t
  vy = v0y + ay*t
  x2 = x + vx*t + (ax*pow(t,2))/2
  y2 = y + vy*t + (ay*pow(t,2))/2
  x01 = x0 + v*t1
  y01 = y0 + v1*t1
  x00.append(x01)
  y00.append(y01)
  x1.append(x2)
  y1.append(y2)
  x = x2
  y = y2
  x0 = x01
  y0 = y01
  v0x = vx
  v0y = vy
  t1 = t1+t
  i = i +1

plot(x1,y1,'-.',color='black',label='Path followed by charge q2',linewidth=0.8)
plot(x00,y00,'--')
plot(x00[0],y00[0],'o')
plot(x0,y0,'o',color='blue',label='Fixed charge q1')
plot(x1[0],y1[0],'o',color='red',label='Initial position of charge q2')
plot(x,y,'o',color='green',label='final position of charge q2')
legend()
xlabel('x Position of the mass')
ylabel('y Position of the mass')
suptitle('Plot of Path followed by charge q2 in particle frame')
show()
