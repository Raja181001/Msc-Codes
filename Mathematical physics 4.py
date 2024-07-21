from numpy import *
from matplotlib.pyplot import *

def dprey(n,p,a,b):
    return p*(a-(b*n))

def dpredator(n,p,c,d):
    return n*(-c+(d*p))


#Intial Number of Prey and Predator
predator_=[9]
prey_=[20]
t=[0]
a = 0.2
b = 0.025
c = 0.1
d = 0.02
i=0
while i <20000:
    dt = 0.01
    predator_.append(predator_[i]+dprey(prey_[i],predator_[i],a,b)*dt)
    prey_.append(prey_[i]+dt*dpredator(prey_[i],predator_[i],c,d))
    t.append(t[i]+dt)
    i+=1

figure('Prey and Predator population wrt time')
plot(t,predator_,'--',color='black',label='Prey population')
plot(t,prey_,'--',color='red',label='Predator population')
xlabel('Time',fontsize=15)
ylabel('Population',fontsize=15)
title('Rate of Change of Prey and Predator Population with Time',fontsize=15)
legend(loc='best')

figure('Relation between prey and Predator')
plot(prey_,predator_,color='black',linewidth=0.5,label='Predator Prey population')
xlabel('Predator',fontsize=15)
ylabel('Prey',fontsize=15)
title('Phase Diagram between Prey and Predator',fontsize=15)
scatter(prey_[0],predator_[0],color='red',label='Initial Population')
scatter(prey_[-1],predator_[-1],color='green',label='Final population')
legend()
show()
