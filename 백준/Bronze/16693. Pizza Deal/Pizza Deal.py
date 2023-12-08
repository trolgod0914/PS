from math import *
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())
W, P = R1**2*pi/P2, A1/P1
if W > P:
    print('Whole pizza')
else:
    print('Slice of pizza')