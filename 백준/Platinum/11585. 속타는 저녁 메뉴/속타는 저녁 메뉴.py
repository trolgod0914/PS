import math

def KMP(target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    return Array[l-1]

N = int(input())
S = input().split()
T = input().split()
K = KMP(S)
A1 = 1 if N%(N-K) else N//(N-K)
A2 = N
GCD = math.gcd(A1, A2)
A1 //= GCD
A2 //= GCD
print('{}/{}'.format(A1, A2))