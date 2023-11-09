import sys, math
input = sys.stdin.readline
print = sys.stdout.write
import operator
from functools import reduce

N, M, K = map(int, input().split())

def Combination(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(operator.mul, range(n, n-r, -1), 1)
    denominator = reduce(operator.mul, range(1, r+1), 1)
    return numerator // denominator

Answer = 0
if K == 0:
    Answer = 1
else:
    for i in range(M+1):
        if K >= i*(N+1):
            Answer += ((-1)**(i%2))*Combination(M, i)*Combination(M+K-i*(N+1)-1, K-i*(N+1))
print(str(Answer%1000000009))