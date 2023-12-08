from math import *
while True:
    a, b = map(float, input().split())
    if a > 0 and b > 0:
        print('Q1')
    if a < 0 and b > 0:
        print('Q2')
    if a < 0 and b < 0:
        print('Q3')
    if a > 0 and b < 0:
        print('Q4')
    if a == 0 or b == 0:
        print('AXIS')
        if a == b:
            exit()