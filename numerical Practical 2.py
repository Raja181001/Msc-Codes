from matplotlib.pyplot import *
from numpy import *
from pandas import *
#Defining all the required functions
def problem1(x,y):               # function for solving dy/dx = x+y
    return x+y

def problem2(x,y):               # function for solving dy/dx = 6xy^2
    return 6*x*square(y)

def circuit(i):                  # function for solving the current flowing through L-R series circuit
    V,R,L=1,1,1
    return (V-i*R)/L

def error(x,y):                 # fnction to calculate the relative error in the numerical method comparing with the analytic method
    return round((1-(y/x))*100,2)



# defining different array of step size using which we calculate the numerical solution
h = [0.5,0.01,0.001]




# for solving the first problem and plotting
j=0
data1 = []
while j<len(h):
    st = 0
    sp = 10
    n = (sp-st)/h[j]
    x = [0]
    y = [1]
    z = [1]
    i = 0
    while i< n:
        x.append(x[i]+h[j])
        y.append(y[i]+h[j]*problem1(x[i],y[i]))
        i+=1
    figure(1)
    z = - x[i] -1 +2*exp(x[i])
    plot(x,y,'-.',label='Numerical Solution with step size = '+str(h[j])+'\n Relative Error at y('+str(round(x[i]))+') = '+str(error(z,y[i]))+'%')
    data1.append([h[j],'y(10) = '+str(round(z,4)),'y(10) = '+str(round(y[i],4)),error(z,y[i])])
    j+=1
scatter(x[i],z,label='Analytical solution at y('+str(round(x[i]))+')')
legend(fontsize='20')
xlabel('x',fontsize='25')
ylabel('solution of the ODE as a function of x [y(x)]',fontsize='25')
title('Numerical Solution of the differential Equation\n $\\frac{dy}{dx} = y + x$',fontsize='20')
axhline(color='black',linewidth='0.5')
axvline(color='black',linewidth='0.5')
grid(True,linewidth=0.3)


#print(data1)

# solving the second question and plotting
j=0
data = []
while j<len(h):
    st = 1
    sp = 3
    n = (sp-st)/h[j]
    x = [1]
    y = [1/25]
    i = 0
    while i< n:
        x.append(x[i]+h[j])
        y.append(y[i]+h[j]*problem2(x[i],y[i]))
        i+=1
    figure(2)
    z = - (1/(3*square(x[i])-28))
    plot(x,y,'-.',label='Numerical Solution with step size = '+str(h[j])+'\n Relative Error at y('+str(round(x[i]))+') = '+str(error(z,y[i]))+'%')
    data.append([h[j],'y(3) = '+str(round(z)),'y(3) = '+str(round(y[i],4)),error(z,y[i])])
    j+=1

scatter(x[i],z,label='Analytical solution at y('+str(round(x[i]))+')')
legend(fontsize='20')
xlabel('x',fontsize='25')
ylabel('solution of the ODE as a function of x [y(x)]',fontsize='25')
title('Numerical Solution of the differential Equation\n $\\frac{dy}{dx} = 6xy^2$',fontsize='20')
axhline(color='black',linewidth='0.5')
axvline(x=1,color='black',linewidth='0.5')
grid(True,linewidth=0.3)


# solving the current problem
st = 0
sp = 10
n = (sp-st)/0.001
x = [0]
y = [0]
i = 0
while i< n:
    x.append(x[i]+0.001)
    y.append(y[i]+0.001*circuit(y[i]))
    i+=1
figure(3)
plot(x,y,)
xlabel('Time  (t)',fontsize='25')
ylabel('Current as a function of Time [I(t)]',fontsize='25')
title('Time Vs Current in a L-R Series',fontsize='25')
axhline(color='black',linewidth='0.5')
axvline(color='black',linewidth='0.5')
grid(True,linewidth=0.3)


# Getting the output in Tabular Form
headers = ['Step size','Analytic solution','Numerical solution','relative error (%)']
df = DataFrame(data , columns=headers)
df1 = DataFrame(data1, columns=headers)
print()
print('Problem 1 : dy/dx = y + x')
print(df1.to_markdown(index=False))
print()
print('Problem 2 : dy/dx = 6xy^2')
print(df.to_markdown(index=False))

show()
