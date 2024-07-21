from numpy import *
from scipy.constants import *
from matplotlib.pyplot import *

def Ydir(q,E,X,m,v):
  y = (q*E*pow(X,2))/(2*m*pow(v,2))
  return y

q = e
m = electron_mass
v = linspace(0.1,5,20)
X = 5
E = -pow(10,-12)
y = []
for i in range(20):
  y1 = Ydir(q,E,X,m,v[i])
  y.append(y1)
  i=+1
ylim(-5,5)
plot(v,y,'.')
axhline(0,color='black')
xlabel('horizontal velocity(m/s)')
ylabel('Position on vertical Screen (m)')
title('Plot of particle hitting a vertical screen across the initial horizontal velocity')
legend(['Position of particle in vertical screen'])
show()