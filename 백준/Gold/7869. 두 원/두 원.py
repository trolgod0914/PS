from math import *
x1, y1, r1, x2, y2, r2 = map(float, input().split())
D = sqrt((x1-x2)**2 + (y1-y2)**2)
R1, R2 = max(r1, r2), min(r1, r2)
if D >= R1+R2:
    Answer = 0
elif D + R2 <= R1:
    Answer = pi*R2*R2
else:
    theta1 = acos((R1**2+D**2-R2**2)/(2*R1*D))
    theta2 = acos((R2**2+D**2-R1**2)/(2*R2*D))
    Circular_Sector1 = R1*R1*theta1
    Circular_Sector2 = R2*R2*theta2
    triangle1 = R1*R1*sin(theta1)*cos(theta1)
    triangle2 = R2*R2*sin(theta2)*cos(theta2)
    Answer = Circular_Sector1+Circular_Sector2-triangle1-triangle2
print("{:.3f}".format(Answer))