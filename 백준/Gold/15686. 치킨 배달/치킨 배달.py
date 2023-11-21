import sys, copy; input = sys.stdin.readline; sys.setrecursionlimit(10000)
from itertools import combinations

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Check = [[0]*N for __ in range(N)]
Chicken = []
House = []

num_1, num_2 = 0, 0
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            House.append((i, j, num_1))
            num_1 += 1
        if Map[i][j] == 2:
            Chicken.append((i, j, num_2))
            num_2 += 1

K = len(Chicken)
Close = []
for k in list(combinations(Chicken, K-M)):
    Close.append([*k])

Record = [[0]*K for _ in range(len(House))]

for a, b, c in House:
    for d, e, f in Chicken:
        Record[c][f] = abs(a-d) + abs(b-e)

Answer = int(1e9)
for A in Close:
    Sum = 0
    Array = copy.deepcopy(Record)
    for B, C, D in A:
        for E in Array:
            E[D] = 2501
    for F in Array:
        Sum += min(F)
    if Answer > Sum:
        Answer = Sum
print(Answer)