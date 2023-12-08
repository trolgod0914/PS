import operator as op
from functools import reduce
N, K = map(int, input().split())
M = int(1e9+7)
def Combination(n, r):
    if n == 0 and r == 0:
        return 1
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

print(Combination(N, K)%M)