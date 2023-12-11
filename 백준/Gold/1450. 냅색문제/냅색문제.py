import sys; input = sys.stdin.readline
from itertools import combinations
from bisect import *
N, C = map(int, input().split())
Array = list(map(int, input().split()))
Left, Right = Array[:len(Array)//2], Array[len(Array)//2:]
S1, S2 = [0], [0]

for i in Left:
    if i <= C:
        S1.append(i)

for i in Right:
    if i <= C:
        S2.append(i)

for i in range(2 ,len(Left)+1):
    L1 = list(combinations(Left, i))
    for j in L1:
        if (S:=sum(j)) <= C:
            S1.append(S)

for i in range(2, len(Right)+1):
    L2 = list(combinations(Right, i))
    for j in L2:
        if (S:=sum(j)) <= C:
            S2.append(S)

S2.sort()
Answer = 0
for k in S1:
    Answer += bisect_right(S2, C-k)

print(Answer)