from numpy import *
from matplotlib.pyplot import *
from scipy.linalg import *


n = 2000
d = 1/n
x = linspace(-1,1,n+1)

def potential(x):
    return x**2


V = potential(x)
d1 = 2 + 2*(d**2)*potential(x)[1:-1]
e = -ones(len(d1)-1)
ev , ef = eigh_tridiagonal(d1,e)
plot(x[1:-1],ef.T[0])
plot(x[1:-1],ef.T[1])
plot(x[1:-1],ef.T[2])
plot(x[1:-1],ef.T[3])
plot(x[1:-1],ef.T[4])
plot(x[1:-1],ef.T[5])

show()