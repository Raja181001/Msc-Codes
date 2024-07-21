from matplotlib.pyplot import *
from numpy import *


# Defining the function for integration
def function(x):  # Function of activity 1
    y = cos(x)**3
    y1 = x**2 + 1
    y2 = sqrt(x)
    return y , y1,y2
def acceleration(t): # Function for activity 2
    if 0<t<5:
        return 0
    elif 5<t<10:
        return 5
    elif 10<t<15:
        return 0
    elif 15<t<20:
        return -5
    elif 20<t<25:
        return 0


rcParams['figure.max_open_warning'] = 50  # This code is to add large number of graph output
# This two arrays are for giving different label to the particular graph
y1label=['$cos^3(x)$','$x^2 + 1$','$\\sqrt{x}$']
int_ylabel = ['$\\int_{-\\pi}^{\\pi}cos^3(x) dx$','$\\int_{-2}^{4}x^2 + 1 dx$','$\\int_{3}^{9}\\sqrt{x} dx$']


# Defining Function For plotting Midpoint Numerical Integration Method
def Midpoint(z,n):
    l = 0
    print('number of steps '+str(n))
    while l<len(data):
        n = n
        a ,b =z[l]
        dx = (b-a)/n
        i = 0
        sum = 0
        x,f,int_f = [],[],[]
        while i < n:
            mid = a + (i+1/2)*dx
            x.append(mid)
            f.append(function(mid)[l])
            sum = sum + dx*function(mid)[l]
            int_f.append(sum)
            i+=1
        figure()
        subplot(2,1,1)
        plot(x,f)
        ylabel(y1label[l],fontsize=20)
        subplot(2,1,2)
        plot(x,int_f)
        ylabel(int_ylabel[l],fontsize=20)
        xlabel('x-values',fontsize=20)
        suptitle('Midpoint Integration For number of step  = ' + str(n), fontsize=20)
        print(abs(round(sum,4)))
        l+=1



# defining Function For plotting Trapezoidal Numerical Integration Method
def Tra(z,n):
    l = 0
    print('number of steps '+str(n))
    while l<len(z):
        n = n
        a , b = z[l]
        dx = (b-a)/n
        sum = 0
        x, f, int_f = [], [], []
        i = 0
        while i < n :
            x1 = a + i*dx
            x2 = x1 + dx
            sum = sum + dx*((function(x1)[l]+function(x2)[l])/2)
            x.append((x1+x2)/2)
            f.append(((function(x1)[l]+function(x2)[l])/2))
            int_f.append(sum)
            i+=1
        figure()
        subplot(2,1,1)
        plot(x,f)
        ylabel(y1label[l],fontsize=20)
        subplot(2,1,2)
        plot(x,int_f)
        ylabel(int_ylabel[l],fontsize=20)
        xlabel('x-values',fontsize=20)
        suptitle('Trapezoidal Integration For number of step  = ' + str(n), fontsize=20)
        print(abs(round(sum,4)))
        l+=1

# Creating a Loop for taking different step numbers
h = [5,10,15,20,50]
data = [[-pi,pi],[-2,4],[3,9]]
k=0
while k < len(h):
    print()
    print()
    print('Midpoint Method')
    Midpoint(data,h[k])
    print('Trapezoidal Method')
    Tra(data,h[k])
    k+=1

# Code for Solving The acceleration Problem
n = 5000
a, b = 0,25
dx = (b - a) / n
i = 0
sum = 0
s1 = 0
x, f, int_f,d= [], [], [],[]
while i < n:
    mid = a + (i + 1 / 2) * dx
    x.append(mid)
    f.append(acceleration(mid))
    sum = sum + dx * acceleration(mid)
    s1 = s1 + dx*sum
    d.append(s1)
    int_f.append(sum)
    i += 1
figure()
subplot(3, 1, 1)
plot(x, f)
ylabel('acceleration',fontsize=18,labelpad=10)
subplot(3, 1, 2)
plot(x, int_f)
ylabel('velocity',fontsize=18,labelpad=10)
subplot(3,1,3)
ylabel('displacement',fontsize=18,labelpad=2)
plot(x,d)
xlabel('Time',fontsize=25)

show()