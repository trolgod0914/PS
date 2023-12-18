import sys, math; input = sys.stdin.readline
N = int(input())
for i in range(1, N+1):
    Array = list(map(int, input().split()))
    Array.sort()
    A, B, C = Array[0], Array[1], Array[2]
    if A == B and B == C:
        print('Case #{}: equilateral'.format(i))
    elif A+B <= C:
        print('Case #{}: invalid!'.format(i))
    elif A == B or B == C or C == A:
        print('Case #{}: isosceles'.format(i))
    else:
        print('Case #{}: scalene'.format(i))    