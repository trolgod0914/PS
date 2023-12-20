from math import *
X, Y, D, T = map(int, input().split())
R = sqrt(X**2+Y**2)
if R >= D:
    A = R//D
    print(min(A*T+R%D, (A+1)*T, R))
else:
    print(min(T + (D-R), 2*T, R))