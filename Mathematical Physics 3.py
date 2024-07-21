from numpy import *
from matplotlib.pyplot import *

x = 3
y = 4

v= [x,y]
x1 = [0,v[0]]
y1 = [0,v[1]]
vect = transpose(v)

theta = -pi/4


# loop for Matrix multiplication
def ROT(th,vect):
    i = 0
    rot = []
    matrix = array([[cos(th),sin(th)],[-sin(th),cos(th)]])
    while i < len(matrix):
        j = 0
        s = 0  # To initialize the value for matrix multiplication
        while j < len(matrix[i]):
            s = s+(matrix[j][i]*vect[j])            # the matrix multiplication

            j+=1
        rot.append(s)
        i+=1
    return rot
def REF(theta,vect):
    ref = []
    i=0
    Ref_matrix = array([[cos(2 * theta), sin(2 * theta)],[sin(2 * theta), -cos(2 * theta)]])
    # loop for Matrix multiplication
    while i < len(Ref_matrix):
        j = 0
        s = 0  # To initialize the value for matrix multiplication
        while j < len(Ref_matrix[i]):
            s = s+(Ref_matrix[j][i]*vect[j])            # the matrix multiplication

            j+=1
        ref.append(s)
        i+=1
    return ref
th1 = pi/2
rot = ROT(th1,vect)
theta = -pi/4
ref = REF(theta,vect)
x2 = [0,rot[0]]
y2 = [0,rot[1]]
x3 = [0,ref[0]]
y3 = [0,ref[1]]
figure('Rotation')
plot(x1,y1,label='Original Vector')
plot(x2,y2,label='Transformed Vector')
title(f'Original vector is rotated by : {th1} degrees',fontsize=25)
legend(fontsize=20)
axis('equal')
figure('Reflection')
plot(x1,y1,label='Original Vector')
plot(x3,y3,label='Reflected Vector')
title('Reflection on line y = -x',fontsize=20)
axis('equal')
legend(fontsize=20)



#analysing the commutative relation
A = 45
B = 30
C = -pi/4
D = pi/4
r1 = REF(D,REF(C,vect))
r3 = REF(C,REF(D,vect))
r2 = ROT(B,ROT(A,vect))
r4 = ROT(A,ROT(B,vect))
x = [0,vect[0]]
y = [0,vect[1]]
x1 = [0,r4[0]]
y1 = [0,r4[1]]
x2 = [0,r2[0]]
y2 = [0,r2[1]]
x3 = [0,r1[0]]
y3 = [0,r1[1]]
x4 = [0,r3[0]]
y4 = [0,r3[1]]
figure()
plot(x,y)
plot(x2,y2,label=f'rotation of {A} degree followed by rotation of {B} degree')
plot(x1,y1,label=f'rotation of {B} degree followed by rotation of {A} degree')
legend()
show()
figure()
plot(x,y,label='original Vector')
plot(x3,y3,label=f'reflection at line of slope {round(tan(C))} followed by reflection at line of slope {round(tan(D))}')
plot(x4,y4,label=f'reflection at line of slope {round(tan(D))} followed by reflection at line of slope {round(tan(C))}')

legend()

show()