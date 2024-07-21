from matplotlib.pyplot import *
from numpy import *
from math import *
from scipy.integrate import quad

def function(a,x,n):
    y1 = ((sqrt(2 / (2 * a)))) * (sin((n * pi * x) / (2 * a)))
    return y1

a = 4
x = linspace(-a,a,1000)
n = 1
while n<=4:
    i=0
    y=[]
    while i<1000:
        y1 = function(a,x[i],n)
        y.append(y1)
        i=i+1
    figure(1)
    plot(x,y,'-.',label='$\Psi_'+str(n)+'$')
    xlabel('x',fontsize='25')
    ylabel('wavefunction ($\Psi_n$)',fontsize='25')
    xlim(-4,4)
    legend(fontsize='15')
    figure(2)
    plot(x,square(y),'-.',label='|$\Psi_'+str(n)+'|^2$')
    ylabel('probability density (|$\Psi_n|^2$)',fontsize='25')
    xlim(-4,4)
    xlabel('x',fontsize='25')
    legend(fontsize='15')
    area, _ = quad(lambda x: abs(function(a, x, n))**2, -a, a)
    print(f'Area under |Ψ_{n}|^2: {area:.4f}')
    n=n+1


show()