from matplotlib.pyplot import *
from numpy import *
def fun(k,m,b,x,v):
  d = -(k/m)*x -b/m(v)
  return d
x = 5
k = 0.1


m = 10
b = 2*sqrt(k*m)
i = 1
y = [x]
t = [0]
v = [0]

ti = 0
tf = 1000
n = 10000
dt = (tf-ti)/n
while i<n :
  v1 = v[i-1] + dt*fun(k,m,b,y[i-1],v[i-1])
  v.append(v1)
  y1 = y[i-1] + dt*v[i-1]
  y.append(y1)
  t1 = t[i-1] + dt
  t.append(t1)
  i+=1

plot(t,y)
xlabel('Time')
ylabel('Displacement')
title('Time VS Displacement Graph with damping')
show()