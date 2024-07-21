from numpy import *
from matplotlib.pyplot import *
from pandas import *
def f(x):
    y = sqrt(x)*exp(-x)
    y1 = (sin(x)**2)/(cos(x))
    y2 = (x**2)/(sqrt(x**3+1))
    return y, y1,y2
data=[[0.2,2],[0,pi],[0.2,2]]
n = [5,10,15,20,50]
print()
# This statement is to give suitable Label for each graph plotted
derv_ylabel = ['$\\frac{d }{dx}(\\sqrt{x}*e^{-x})$','$\\frac{d }{dx}(\\frac{sin(x)^2}{cos(x)})$',
               '$\\frac{d }{dx}(\\frac{x^2}{\\sqrt{x^3 +1}})$']
f_ylabel=['$\\sqrt{x}*e^{-x}$','$\\frac{sin(x)^2}{cos(x)}$',
          '$\\frac{x^2}{\\sqrt{x^3 +1}}$']

# this is a empty list created to tabulate the values of the derivatives
sol = [['1','','','','',''],['2','','','','',''],['3','','','','','']]
j = 0
while j < len(data): # this loop specifies the function and the range to take the derivative
    figure(j+1)

    k = 0
    while k<len(n): # this loop specifies the number of step in which the derivative will be taken
        x_st= float(data[j][0])
        x_en=float(data[j][1])
        x = linspace(x_st,x_en,n[k])
        h = (x_en - x_st)/n[k]
        i =0
        y = f(x)
        y1 = []
        while i < len(x)-2: # loop where the actual derivative is calculates at a point
            t = (4*f(x[i+1])[j]-f(x[i+2])[j]-3*f(x[i])[j])/(2*h)
            y1.append(t)
            i+=1
        sol[j][k + 1] = t  # appends to get the out put in the tabular form
        # plotting
        suptitle('plotting the function and is Derivative',fontsize=20)
        subplot(2,1,2)
        title('Numerical Derivative of the function changing the number of steps',fontsize=15)
        plot(x[0:len(x)-2],y1,label='no. of steps = '+str(n[k]),)
        ylabel(derv_ylabel[j],fontsize=20)
        xlabel('X values', fontsize=20)
        legend()

        k+=1
    # plotting the function

    subplot(2, 1, 1)
    title('Function',fontsize=15)
    plot(x, y[j])
    ylabel(f_ylabel[j],fontsize=20)

    j+=1
#plot(x[0:48],y1)
headers = ['question no.','no. of steps = 5','no. of steps = 10','no. of steps = 15','no. of steps = 20',
           'no. of steps = 50']

print('')
df = DataFrame(sol , columns=headers)
print(df.to_markdown(index=False))

# code finding the minimum Electric Filed
def function(Q,r): # Defining the Function for the electrostat potential
    V = -Q/r
    return V

# initalizing the values
Q = 4
Q1= 2*Q
x_st = 1
x_en = 5
n =100
x = linspace(x_st,x_en,n)
x1 = linspace(x_en,x_st,n)
h = (x_en-x_st)/n
i=0
y1=[]
# t : For finding the Electric field due to point charge Q
# t1 : For finding teh Electric Filed due to point charge Q1
# and then we take the absolute value of teh Electric filed and plot to analyse
while i < len(x) - 2:
    t = (4 * function(Q,x[i + 1]) - function(Q,x[i + 2]) - 3 * function(Q,x[i])) / (2 * h)
    t1 = (4 * function(Q1,x1[i + 1]) - function(Q1,x1[i + 2]) - 3 * function(Q1,x1[i])) / (2 * h)
    y1.append(abs(t1-t))
    i += 1
print('The minimum value of the electric filed is : '+str(min(y1)))
print('The Electric field is minimum at x = '+str(round(x[y1.index(min(y1))],4)))
plot(x[0:n-2],y1,'--',color='black',label='Electric filed at different distance between the point charge in x-axis')
xlabel('Distance between two point charge ',fontsize=20)
ylabel('Magnitude of the electric field between two points',fontsize=20)
scatter(x[y1.index(min(y1))],min(y1),color='red',label='point of minimum Electric Field')
title('Analysing the Electric Filed between two points along the x-axis',fontsize=20)
legend(fontsize=20)
show()

