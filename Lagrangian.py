from numpy import *
from matplotlib.pyplot import *



def Solve(g, m1, m2, l1, l2, t1, t2, t1_d, t2_d):
    n = ((m2 * g * sin(t2) * cos(t1 - t2)) - (m2 * sin(t1 - t2) * (l1 * (t1_d ** 2) * cos(t1 - t2) + l2 * (t2_d) ** 2)) - ((m1 + m2) * g * sin(t1)))
    d = (l1 * (m1 + m2 * ((sin(t1 - t2)) ** 2)))
    z1 = (n / d)
    n1 = (((m1 + m2) * (l1 * ((t1_d) ** 2) * sin(t1 - t2) - g * sin(t2) + (g * sin(t1) * cos(t1 - t2)))) + (m2 * l2 * ((t2_d) ** 2) * sin(t1 - t2) * cos(t1 - t2)))
    d1 = (l2 * (m1 + m2 * ((sin(t1 - t2)) ** 2)))
    z2 = (n1 / d1)
    z3 = t1_d
    z4 = t2_d
    return z1, z2, z3, z4

ti = 0

n=40000
dt = 0.001
g= 9.81
m1=2
m2=1
l1=2
l2=1
j = 1
t= [ti]
t1_d=[1]
t2_d=[-1]
t1=[pi/2]
t2=[(3*pi)/2]
j = 1
while j < n:
  v1 = t1_d[j-1] + dt * (Solve(g, m1, m2, l1, l2, t1[j-1], t2[j-1], t1_d[j-1], t2_d[j-1])[0])
  t1_d.append(v1)
  v2 = t2_d[j-1] + dt * (Solve(g, m1, m2, l1, l2, t1[j-1], t2[j-1], t1_d[j-1], t2_d[j-1])[1])
  t2_d.append(v2)
  y1 = t1[j-1] + dt*(Solve(g, m1, m2, l1, l2, t1[j-1], t2[j-1], t1_d[j-1], t2_d[j-1])[2])
  t1.append(y1)
  y2 = t2[j-1] + dt*(Solve(g, m1, m2, l1, l2, t1[j-1], t2[j-1], t1_d[j-1], t2_d[j-1])[3])
  t2.append(y2)
  tt = t[j-1]+dt
  t.append(tt)
  j =j+ 1

y1 = -l1*cos(t1)
x1 = l1*sin(t1)
x2 = l1*sin(t1)+l2*sin(t2)
y2 = -l1*cos(t1)-l2*cos(t2)
figure(1)
title('Double Pendulum motion graph of $\Theta$ Vs t',fontsize='25')
suptitle('Intial condition : $\Theta$$_1$(0) :- '+str(round(t1[0],3))+'rad  $\Theta$$_2$(0) :- '+str(round(t2[0],3))+'rad  $\Theta$$^{(1)}_1$(0) : '+str(round(t1_d[0],3))+
         '$\\frac{rad}{sec}$  $\Theta$$^{(1)}_1$(0) : '+str(round(t2_d[0],3))+'$\\frac{rad}{sec}$',fontsize='20')
plot(t,t2,label='mass 2',color='red')
plot(t,t1,label='mass 1',color='black')
ylabel('Angle Suspended from vertical ($\Theta$(t) : radian)',fontsize='25')
xlabel('Time (t : sec)',fontsize='25')
axhline(color='blue',linewidth='0.5')
axvline(color='blue',linewidth='0.5')
legend(fontsize='25')
xlim(-1,t[n-1])
grid()
figure(2)
title('Double Pendulum motion graph of x Vs y co-ordinates of the masses',fontsize='25')
suptitle('Intial condition : $\Theta$$_1$(0) :- '+str(round(t1[0],3))+'rad  $\Theta$$_2$(0) :- '+str(round(t2[0],3))+'rad  $\Theta$$^{(1)}_1$(0) : '+str(round(t1_d[0],3))+
         '$\\frac{rad}{sec}$  $\Theta$$^{(1)}_1$(0) : '+str(round(t2_d[0],3))+'$\\frac{rad}{sec}$',fontsize='20')
axis('equal')
plot(x1,y1,label='mass 1',color='black')
plot(x2,y2,'-.',label='mass 2',color='red')
plot(x1[0],y1[0],'.',color='blue',markersize='15',label='Initial Position of m1')
plot(x2[0],y2[0],'.',color='black',markersize='15',label='Initial Position of m2')
plot(x2[n-1],y2[n-1],'.',color='purple',markersize='15',label='Final Position of m2')
plot(x1[n-1],y1[n-1],'.',color='green',markersize='15',label='Final Position of m1')
plot(0,0,'.',markersize='20',color='violet',label='Pivot point')
xlabel('X Co-ordinate',fontsize='25')
ylabel('Y Co-ordinate',fontsize='25')
axhline(color='blue',linewidth='0.5')
axvline(color='blue',linewidth='0.5')
#lim(-maximum(l1,l2),maximum(l1,l2))
#ylim(-maximum(l1,l2)-1,maximum(l1,l2)+1)
axis('equal')
legend(fontsize='15')
grid()
show()