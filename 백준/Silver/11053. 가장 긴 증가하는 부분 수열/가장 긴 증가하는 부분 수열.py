from bisect import *
import sys; input = sys.stdin.readline

N = int(input())
Sequence = list(map(int, input().split()))
Answer = 1
LIS = [Sequence[0]]

for i in range(1, N):
    if Sequence[i] > LIS[-1]:
        LIS.append(Sequence[i])
        Answer += 1
    else:
        LIS[bisect_left(LIS, Sequence[i]) ] = Sequence[i]

print(Answer)