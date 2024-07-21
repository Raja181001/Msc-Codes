from matplotlib.pyplot import *
from numpy import *
from math import *


def Bessel(x,n):
    m= 0
    s=0
    while m <30:
        nu = ((-1)**m) * (x**(2*m + n))
        de = (2**(2*m + n)) * factorial(m) * factorial(n + m)
        s = s + (nu/de)
        m+=1
    return s


def Hermite(x,n):
    l = 0
    s = 0
    if (n%2) == 0:
        while l <= (n/2):
            nu = ((factorial(n))*power((-1),((n/2)-l))*power(2*x,2*l))
            de = ((factorial(2*l))*(factorial(int(n/2)-l)))
            s = s + (nu/de)
            l+=1
        return s
    else:
        while l <= (n-1)/2:
            nu = ((factorial(n))*power((-1),(((n-1)/2)-l))*power(2*x,2*l+1))
            de = ((factorial(2*l+1))*(factorial(int((n-1)/2)-l)))
            s = s + (nu/de)
            l+=1
        return s



def Lagurre(x,n):
    s=0
    k=0
    while k<=n:
        nu = factorial(n)*((-1)**k)*(x**k)
        de = (factorial(k))*(factorial(n-k))*factorial(k)
        s = s + (nu/de)
        k+=1
    return s



def Legendre(x,n):
    s = 0
    m=0
    while m <= n//2:
        de = (power(2,n)*factorial(m)*factorial(n-m)*factorial(n-2*m))
        nu = (power(-1,m)*factorial(2*n - 2*m)*power(x,n-2*m))
        s = s + (nu/de)
        m=m+1
    return s



figure(1)
ns = 1000
x = linspace(-20,20,1000)
n = 0
while n <= 5:
    y = Bessel(x,n)
    plot(x,y,'-.',label='$J_'+str(n)+'$(x)')
    n = n+1

title('First 5 orders of Bessel polynomial of first kind',fontsize='25')
xlim(-1,20)
ylim(-1,1)
axhline(0,color='black',linewidth='0.5')
axvline(0,color='black',linewidth='0.5')
xlabel('x',fontsize='25')
ylabel('Bessel polynomial of first kind ($J_n(x)$)', fontsize='25')
legend(fontsize='20',loc='upper right')



figure(2)
ns = 1000
x = linspace(-5,5,1000)
n = 0
while n <= 5:
    y = Hermite(x,n)
    plot(x,y,'-.',label='$H_'+str(n)+'$(x)')
    n = n+1



title('First 5 order of Hermite polynomials',fontsize='25')
ylim(-160,160)
xlim(-5,5)
axhline(0,color='black',linewidth='0.5')
axvline(0,color='black',linewidth='0.5')
xlabel('x',fontsize='25')
ylabel('Hermite polynomial $H_n(x)$',fontsize='25')
legend(fontsize='25',loc='lower right')




figure(3)
ns = 1000
x = linspace(-5,20,1000)
n = 0
while n <= 5:
    y = Lagurre(x,n)
    plot(x,y,'-.',label='$L_'+str(n)+'$(x)')
    n = n+1



title('First 5 orders of Laguerre polynomial',fontsize='25')
ylim(-15,45)
xlim(-5,20)
axhline(0,color='black',linewidth='0.5')
axvline(0,color='black',linewidth='0.5')
xlabel('x',fontsize='25')
ylabel('Laguerre Polynomial ($L_n(x)$)',fontsize='25')
legend(fontsize='25',loc='upper right')





figure(4)
ns = 1000
x = linspace(-1,1,1000)
n = 0
while n <= 5:
    y = Legendre(x,n)
    plot(x,y,'-.',label='$P_'+str(n)+'$(x)')
    n = n+1

title('First 5 order of Legendre polynomials',fontsize='25')
axhline(0,color='black',linewidth='0.5')
axvline(0,color='black',linewidth='0.5')
xlabel('x',fontsize=25)
ylabel('Legendre polynomial ($P_n(x)$)',fontsize='25')
legend(fontsize='19',loc='lower right')
show()
