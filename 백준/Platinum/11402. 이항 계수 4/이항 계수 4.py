import operator as op
from functools import reduce
N, K, M = map(int, input().split())

def Trans_Radix(Num, Radix):
    Array = [0]*50
    Index = 0
    while Num > 0:
        Array[Index] = Num%Radix
        Num //= Radix
        Index += 1
    return Array

def Combination(n, r):
    if n == 0 and r == 0:
        return 1
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

N_record = Trans_Radix(N, M)
K_record = Trans_Radix(K, M)
Answer = 1
for i in range(50):
    n, k = N_record[i], K_record[i]
    if k > n:
        Answer = 0
        break
    else:
        Answer = (Answer * Combination(n, k)) % M
print(Answer)