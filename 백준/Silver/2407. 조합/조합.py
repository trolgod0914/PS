import operator
from functools import reduce

N, M = map(int, input().split())

def Combination(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(operator.mul, range(n, n-r, -1), 1)
    denominator = reduce(operator.mul, range(1, r+1), 1)
    return numerator // denominator

print(Combination(N, M))