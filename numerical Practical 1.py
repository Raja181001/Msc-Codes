from matplotlib.pyplot import *
from numpy import *


def circle(r,th):
    x = r*cos(th)
    y = r*sin(th)
    return x,y

def ellipse(x_coff,y_coff,const,th):
    a = sqrt(const/x_coff)
    b = sqrt(const/y_coff)
    x1 = a * cos(th)
    y1 = b * sin(th)
    return x1,y1

def parabolla(x_coff,y_coff,th):
    if x_coff == 0:
        if abs(y_coff) == y_coff:
            x,y = 2*y_coff*th , -y_coff*square(th)
            return x,y
        else :
            x,y = 2*y_coff*th ,-y_coff*square(th)
            return x,y
    if y_coff ==0:
        if x_coff<0:
            y, x = 2 * x_coff * th, - x_coff * square(th)
            return x,y
        else:
            y, x = 2 * x_coff * th, - x_coff * square(th)
            return x,y

def hyperbola(x_coff,y_coff,const,th):
    if x_coff <0:
        a = sqrt(const/abs(y_coff))
        b = sqrt(const/abs(x_coff))
        y = a*(1/cos(th))
        x = b*tan(th)
        return x,y
    else:
        a = sqrt(const/x_coff)
        b = sqrt(const/y_coff)
        x = a*(1/cos(th))
        y = b*tan(th)
        return x,y



# plotting the circle
figure(1)
th=linspace(0,2*pi,1000)
r =1
plot(circle(r,th)[0],circle(r,th)[1])
axis('equal')
xlabel('x values',fontsize='25')
ylabel('Circle y(x)',fontsize='25')
title('Plotting Circle',fontsize='25')


# plotting the ellipse
figure(2)
x_coff = 169
y_coff = 25
const = 4225
plot(ellipse(x_coff,y_coff,const,th)[0],ellipse(x_coff,y_coff,const,th)[1])
axis('equal')
xlabel('x values',fontsize='25')
ylabel('Ellipse y(x)',fontsize='25')
title('Plotting Ellipse',fontsize='25')


# plotting the parabola
figure(3)
x_coff = 0
y_coff = -4
th = linspace(-pi,pi,1000)
di = full(1000,y_coff)
plot(parabolla(x_coff, y_coff, th)[0],parabolla(x_coff, y_coff, th)[1],label='parabola')
plot(parabolla(x_coff, y_coff, th)[0],di,label='Directrix')
xlim(-25,25)
legend(fontsize='15')
xlabel('x values',fontsize='25')
ylabel('Parabola y(x)',fontsize='25')
title('Plotting Parabola',fontsize='25')


# plotting of hyperbola
figure(4)
x_coff = -2
y_coff = 8
const = 16
plot(hyperbola(x_coff,y_coff,const,th)[0],hyperbola(x_coff,y_coff,const,th)[1],'-.',color='red')
xlim(-13,13)
ylim(-7,7)
xlabel('x values',fontsize='25')
ylabel('Hyperbola y(x)',fontsize='25')
title('Plotting Hyperbola',fontsize='25')


# plotting of Helix
figure(5)
ax = axes(projection='3d')
th=linspace(0,6*pi,1000)
r =2
z = linspace(0,1,1000)
plot(circle(r,th)[0],circle(r,th)[1],z,'-',linewidth='3',color='red')
axis('equal')
xlabel('x values',fontsize='20')
ylabel('y values',fontsize='20')
ax.set_zlabel('Propogating \ndirection\n of helix',fontsize='20',labelpad=25)
ax.set_zlim(0,1)
title('Plotting Helix',fontsize='25')


# Plotting the paraBOLOID
figure(6)
ax = axes(projection='3d')
th = linspace(0,2*pi,1000)
#x = linspace(-50,50,1000)
#y = linspace(-50,50,1000)
x = 8*cos(th)
y = 3*sin(th)
x,y = meshgrid(x,y)
z = (x**2)/64 + (y**2)/9
ax.plot_surface(x,y,z,cmap='RdBu')
ax.set_xlabel('x values',fontsize='20')
ax.set_ylabel('y values',fontsize='20')
ax.set_zlabel('Elliptical paraboloid',fontsize='20',labelpad=10)
title('plotting a 3-D function ')
#xlim(-100,100)
#ylim(-100,100)
show()