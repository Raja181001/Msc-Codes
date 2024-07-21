from numpy import *
from math import *
from matplotlib.pyplot import *
from scipy.constants import *
from ipywidgets import interactive
def function(E,V,k,a):
    T = (16*E*(V-E)*exp(-2*k*a))/pow(V,2)
    return T
def func(z,k,a):
    T = (16*z*(1-z))*exp(-2*k*a)
    return T
m = electron_mass
m1 = 2*electron_mass
m2 = 3*electron_mass
x = float(input('Enter the width of the potential barrier-1: '))
x1 = float(input('Enter the width of the potential barrier-2: '))
x2 = float(input('Enter teh width of the potential barrier-3: '))
V = float(input('Enter the height of the potential barrier-1: '))
V1 = float(input('Enter the height of the potential barrier-2: '))
V2 = float(input('Enter the height of the potential barrier-3: '))
E = float(input('Enter the energy of the wave: '))
Ee = E*electron_volt
Vo = V*electron_volt
V1 = V1*electron_volt
V2 = V2*electron_volt
Es = electron_volt
a = x*pow(10,-9)
a1 = x1*pow(10,-9)
a2 = x2*pow(10,-9)
e = linspace(0,Ee,10)
v = linspace(electron_volt,Vo,10)
z=e/Vo
y = []
y1 =[]
y2 =[]
T =[]
print(a)
print(a1)
print(a2)
print(Vo)
print(V1)
print(V2)
print(Ee)
i =0
for i in range (0,10):
    k = sqrt(2*m*(Vo-Ee))/(h/2*pi)
    k1 = sqrt(2*m1*(Vo-e[i]))/(h/2*pi)
    k2 = sqrt(2*m2*(Vo-e[i]))/(h/2*pi)
    r = function(e[i],Vo,k,a)
    r1 = function(e[i],Vo,k1,a)
    r2 = function(e[i],Vo,k2,a)
    r3 = func(z[i],k1,a)
    T.append(r3)
    y.append(r)
    y1.append(r1)
    y2.append(r2)
    i+=1
plot(e,y,label=m,color='red')
plot(e,y1,label=m1,color='black')
plot(e,y2,label=m2,color='green')
xlabel('Energy level')
ylabel('Transmission Coefficient')
title('Transmission coefficient Vs Energy (changing mass of the particle)')
#plot(z,T) #ylim([0,2*pow(10,-18)])
legend  ()
show()
q = []
q1 = []
q2 = []
for j in range (0,10):
    k = sqrt((2 * m * (Vo-e[j]) ) / (pow(h, 2)))
    r = function(e[j],Vo,k,a)
    r1 = function(e[j],Vo,k,a1)
    r2 = function(e[j],Vo,k,a2)
    q.append(r)
    q1.append(r1)
    q2.append(r2)
    j+=1
plot(e,q,label=a,color='green')
plot(e,q1,label=a1,color='black')
plot(e,q2,label=a2,color='red')
title('Transmission coefficient Vs Energy (Changing width of the potential barrier)')
legend()
show()
w = []
w1 = []
w2 = []
j = 0
for j in range (0,10):
    k = sqrt((2 * m * (Vo-e[j]) ) / (pow(h, 2)))
    r = function(e[j],Vo,k,a)
    r1 = function(e[j],V1,k,a)
    r2 = function(e[j],V2,k,a)
    w.append(r)
    w1.append(r1)
    w2.append(r2)
    j+=1
plot(e,w,label=Vo,color='green')
plot(e,w1,label=V1,color='black')
plot(e,w2,label=V2,color='red')
title('Transmission coefficient Vs Energy (Changing height of the potential barrier)')
legend()
show()