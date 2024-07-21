from matplotlib.pyplot import *
from numpy import *




def velocity(g, r, v):
    r = g - (r) * v
    return r

t = linspace(0, 100, 10000)
h = (100 - 0) / 10000
v = [0]
g = 10
y = [0]

for i in range(1, 10000):
    v1 = v[i - 1] + h * velocity(g, r, v[i - 1])
    v.append(v1)

for j in range(1, 10000):
    y1 = y[j - 1] + h * t[j - 1]
    y.append(y1)

figure(figsize=[20, 20])
subplot(3, 2, 1)
plot(t, v)
title('velocity Vs Time')
xlabel('Time (s) ')
ylabel('velocity (m/s) ')

subplot(3, 2, 2)
plot(t, y)
title('Displacement Vs Time')
xlabel('Time (s) ')
ylabel('Displacement (m) ')



