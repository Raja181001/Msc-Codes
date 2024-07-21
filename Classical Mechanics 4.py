from numpy import *
from matplotlib.pyplot import *

# Defining the functions for differentiation and intergration
def derv(x,h):   #function for derivative
    i =0 
    y1 = []
    while i < len(x)-2: 
        t1 = ((4*x[i+1]-x[i+2]-3*x[i])/(2*h))**2
        y1.append(t1)
        i+=1
    return y1


def int(ds,dx):  #function for integration
    int_f = []
    i = 0 
    sum = 0
    while i < len(ds):
        mid = a + (i+1/2)*dx
        sum = sum + dx*ds[i]
        int_f.append(sum)
        i+=1
    return sum

def f(a,t):
    x = a*(t-sin(t))
    y = a*(1-cos(t))
    return x,y



# Plotting the cycloid and calculating the time taken 
a = 2
t = linspace(0,pi,10000)

z = f(a,t)
x = a*(t-sin(t))
y = a*(1-cos(t))
h = (y[-1]-y[0])/len(y)
m = (z[1][-1]-z[1][0])/(z[0][-1]-z[0][0])
sq_x1 = derv(x,h)
sq_y1 = derv(y,h)
ds = sqrt((sq_x1+sq_y1))
t1 = int(ds,h)
print(f'Time taken in the  cycloid path {t1}')
plot(z[0],-z[1],label=f'time taken in the  cycloid path {round(t1,4)}')



# Plotting the straight line and calculating the time taken 
sq_x3 = derv(z[0],h)
sq_y3 = derv(-z[0],h)
ds = sqrt(sq_x3+sq_y3)
t2 = int(ds,h)
print(f'Time in Straight line {t2}')
plot(z[0],-m*z[0],label=f'Time in Straight line {round(t2,4)}')



# Calculating the radius of the circle and plotting the semicircular path and calculating the time taken
r = (sqrt((z[0][-1]-z[0][0])**2+(z[1][-1]-z[1][0])**2))/2
center = (z[0][-1]-z[0][0])/2 , -(z[1][-1]-z[1][0])/2
x = center[0]+r*cos(t)
y = center[1]+r*sin(-t)
angle_degrees = -32.5  
angle_radians = deg2rad(angle_degrees)
'''Apply the rotation transformation to the points of the semicircle'''
x_rotated = center[0] + (x - center[0]) * cos(angle_radians) - (y - center[1]) * sin(angle_radians)
y_rotated = center[1] + (x - center[0]) * sin(angle_radians) + (y - center[1]) * cos(angle_radians)

sq_x2 = derv(x_rotated,h)
sq_y2 = derv(y_rotated,h)
ds = sqrt(sq_x2+sq_y2)

t = int(ds,h)
print(f'Time in Semicircular path is {t}')
plot(x_rotated,y_rotated,label=f'Time in Semicircular path is {round(t,4)}')


# Plotting the Parabolic path

x1 = z[0][0]
x2 = z[0][-1]
y1 = z[1][0]
y2 = z[1][-1]

a = -(y2 - y1) / (x2 - x1)**2
b = -2 * a * x1

# Generate x values
x = linspace(x1, x2, 10000)

# Calculate corresponding y values using the parabolic equation
y = -(a * (x**2) + (b * x))


fixed_point = array([0, 0])

# Define the angle of rotation in radians
angle = -(deg2rad(65))  # Rotate by 45 degrees (pi/4 radians)

# Create a 2D rotation matrix
rotation_matrix = array([[cos(angle), -sin(angle)],
                            [sin(angle), cos(angle)]])

# Apply the rotation matrix to every point on the parabola
rotated_points = []
for point in column_stack((x, y)):
    translated_point = point - fixed_point
    rotated_point = dot(rotation_matrix, translated_point) + fixed_point
    rotated_points.append(rotated_point)

# Convert the list of rotated points back to separate x and y arrays
rotated_x, rotated_y = zip(*rotated_points)

h = (y[-1]-y[0])/(len(y))
sq_x4 = derv(rotated_x,h)
sq_y4 = derv(rotated_y,h)
ds = sqrt((sq_x4+sq_y4))
t = int(ds,h)
print(f'Time taken in the parabolic path is {t}')
plot(rotated_x, rotated_y,label=f'Time taken in the parabolic path is {round(t,4)}')


axis('equal')
legend(fontsize=15)
xlabel('x',fontsize=15)
ylabel('y',fontsize=15)
show()