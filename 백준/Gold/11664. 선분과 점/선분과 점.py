from math import sqrt
x1, y1, z1, x2, y2, z2, x3, y3, z3 = map(int, input().split())
Answer = int(1e9)
while True:
    x4, y4, z4 = (x1+x2)/2, (y1+y2)/2, (z1+z2)/2    
    A = sqrt((x1-x3)**2+(y1-y3)**2+(z1-z3)**2)
    B = sqrt((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)
    C = sqrt((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)
    if abs(Answer-C) <= 1e-6: break
    if C < Answer: Answer = C
    if A < B: x2, y2, z2 = x4, y4, z4
    if A > B: x1, y1, z1 = x4, y4, z4
print(Answer)