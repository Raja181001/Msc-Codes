from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import quad

# define the constants in the function
m = 1
v1 = 1*power(10.0,1)
a = 0.1
hbar = 1



# define functions to plot the wave-function and the probability graph
def wave(x,v,m):
    y1 = (sqrt((m*v)/(square(hbar))))*(exp(-((m*v)/(square(hbar)))*abs(x)))
    return y1
def prob(x,v,m):
    y2 = ((sqrt((m*v)/(square(hbar))))*(exp(-((m*v)/(square(hbar)))*abs(x))))**2
    return y2
def gaussian(x,si,mu):
    y = ((1/(si*sqrt(2*pi))))*(exp((-(x-mu)**2)/(2*square(si))))
    return y



# initialising the value of x
x1 = 0
x = linspace(-15,15,10000)
v = [v1/3,v1/2,v1,v1*2,v1*3]
# x = 0 is not necessarily included in the array created
# we check the inclusion of the x = 0 and if not included we include it into the array at the perfect position
index_to_insert = np.searchsorted(x, x1)
x = np.insert(x, index_to_insert,x1 )



# Plotting the wave-function
figure(1)
i=0
while i<len(v):
    plot(x,wave(x,v[i],m),label='Wave-Funtion of the Particle with $(V_0)$ ='+str(round(v[i],2)))
    i+=1
xlabel('x',fontsize='25')
ylabel('Wavefntion of the particle $(\Psi(x))$',fontsize='25')
axvline(x=a,color='black',linestyle='-.',label='Region of Observation')
axvline(x=-a,color='black',linestyle='-.')
xlim(-a-1,a+1)
ylim(bottom=-1)
grid(True,linewidth='0.3')
axhline(color='black',linewidth='0.5')
axvline(color='black',linewidth='0.5')
# Annotate is used to define a region under which we make our observations
annotate('Region of Observation', xy=(a,0.2), xytext=(0, -.5),arrowprops=dict(facecolor='black', shrink=0.005,linewidth=0.000000001),fontsize='14')
annotate('',xy=(-a,0.2), xytext=(0, -0.4),arrowprops=dict(facecolor='black', shrink=0.05,linewidth=0.000000001))
legend(loc='upper right',fontsize='15')
title('Wave-Function of a particle as function of position (x)',fontsize='25')




# Plotting the Probability density graph
figure(2)
k=0
while k<len(v):
    plot(x, wave(x, v[k], m) ** 2, '-',
         label='Particle with $(V_0)$ ='+str(round(v[k],2)) +'\n Probability of finding the particle \n between ' + str(-a) + '&' + str(a)
               + ' is P: ' + str(round(quad(prob, -a, a, args=((v[k]), m))[0] * 100, 3)) + '%')
    k+=1

axvline(x=a,color='black',linestyle='-.',label='Region of observation')
axvline(x=-a,color='black',linestyle='-.')
# Annotate is used to define a region under which we make our observations
annotate('Region of Observation', xy=(a,1), xytext=(0, -1.5),arrowprops=dict(facecolor='black', shrink=0.05,linewidth=0.000000001),fontsize='14')
annotate('',xy=(-a,1), xytext=(0, -1.2),arrowprops=dict(facecolor='black', shrink=0.05,linewidth=0.000000001))
ylim(bottom=-2)
xlim(-a-1,a+1)
xlabel('x',fontsize='25')
grid(True,linewidth='0.3')
axhline(color='black',linewidth='0.5')
axvline(color='black',linewidth='0.5')
ylabel('Probability distribution function ($|\Psi(x)|^2$)',fontsize='25')
legend(loc='upper right',fontsize='15')
title('Probability distribution of finding a particle at a position')



# The Change in Probability as the a changes
t = linspace(0,5,1000)
j=0
while j <len(v):
    i=0
    y = []
    while i<1000:
        y1 = quad(prob,-t[i],t[i],args=(m,v[j]))[0]
        y.append(y1)
        i+=1
    figure(3)
    plot(t, y,label='particle under dirac potential : '+str(round(v[j],2)))
    legend(fontsize='15')
    j+=1
xlabel('Region of Observation (a)',fontsize='25')
ylabel('Probability of finding particle \n under the potential as a function of a',fontsize='25')
grid(True,linewidth='0.3')
axhline(color='black',linewidth='0.5')
axvline(color='black',linewidth='0.5')
title('Probability of a particle to be bounded as a function of a')



# Gaussian Plot
n=0.2
while n<=1:
    figure(4)
    plot(x,gaussian(x,n,0),'-.',label='$\mu = $'+str(0)+' , $\sigma^2$ = '+str(round(n,3)))
    n+=0.2
ylabel('Gaussian function ($\Phi_{\mu,\sigma^2}(x)$)',fontsize='25')
xlabel('x',fontsize='25')
legend(fontsize='15')
xlim(-7,7)
grid(True,linewidth='0.3')
axhline(color='black',linewidth='0.7')
axvline(color='black',linewidth='0.7')
title('Gaussian Function')

show()