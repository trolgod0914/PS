import operator as op
import math as mt
from functools import reduce

N, C, D, M = map(int, input().split())

def Combination(n, r):
    if r > n or r < 0 or n < 0:
        return 0
    if n == 0 and r == 0:
        return 1
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

DP = [[0]*(N+1) for _ in range(D+1)]
DP[0][0] = 1

for Day in range(1, D+1):
    for Num in range(N+1):
        for num in range(N+1):
            DP[Day][Num] += DP[Day-1][num] * Combination(N-num, Num-num) * Combination(num, C-Num+num)

A = DP[D][M]
B = Combination(N, C) ** D
print(A/B)