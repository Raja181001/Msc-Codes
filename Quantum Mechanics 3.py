from matplotlib.pyplot import *
import numpy as np
import scipy.special as sp
import math as mat

def Radial(n,l,r,a):
    r1 = np.sqrt(np.power((2/(n*a)),3))
    r2 = np.sqrt(mat.factorial(n-l-1)/(2*n*np.power(mat.factorial(n+l),3)))
    r3 = np.power((2*r)/(n*a),l)
    r4 = np.exp(-r/(n*a))
    L = sp.genlaguerre(n - l - 1, 2 * l + 1)(2 * r / (n * a))
    r = r1*r2*r3*r4*L
    return r

def Sperical(l,m,th,phi):
    y = np.sqrt((2*l +1)*mat.factorial(l-m)/(2*np.pi*mat.factorial(l+m)))
    P_mn = sp.lpmn(m,l,np.cos(th))
    L = abs(P_mn[0][m][l])
    y*= L
    if m <0:
        y*=np.cos(m*phi)
    else:
        y*=np.cos(m*phi)
    return y

r = np.linspace(0,10,500)
a = 0.529

n = [1,2,3,4]
for i in range(len(n)):
    l = np.arange(0,n[i])
    figure(i)
    title(f'Radial Wavefunction for the Hydrogen atom with principle quantum number {n[i]}',fontsize=15)
    xlabel('Distance from the nuclei',fontsize=20)
    #ylabel('Electron Density',fontsize=20,labelpad=25)
    for j in range(len(l)):
        subplot(len(l),1,j+1)
        #plot(r,Radial(n[i],l[j],r,a),label=f'n : {n[i]}, l : {l[j]} : Wave function')
        plot(r,r**2*(Radial(n[i],l[j],r**2,a))**2,label=f'n : {n[i]}, l : {l[j]} : Probability Density')
        legend()


for l in range(1,4):
    h = 200
    fig = figure()
    num = 0
    for m in range(-l,l+1):
        num+=1
        phi,theta = np.linspace(0,2*np.pi,h),np.linspace(-np.pi,np.pi,h)
        R = np.zeros((h,h))
        for i in range(h):
            for j in range(h):
                R[i][j] = Sperical(l,m,theta[j],phi[i]).real
        theta,phi = np.meshgrid(theta,phi)
        x = R*np.sin(theta)*np.cos(phi)
        y = R*np.sin(theta)*np.sin(phi)
        z = R*np.cos(theta)
        ax = fig.add_subplot(1,2*l+1,num,projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.plot_surface(x,y,z,cmap=get_cmap('twilight'))
        max = np.max(x)
        if np.max(y)>max:
            max = np.max(y)
        if np.max(z)>max:
            max = np.max(z)
        ax.set_title(f'l = {l} : m ={m}')
        ax.set_xlim(-max,max)
        ax.set_ylim(-max,max)
        ax.set_zlim(-max,max)

    #cbar = fig.colorbar(surf, ax=ax, shrink=0.5)

show()



