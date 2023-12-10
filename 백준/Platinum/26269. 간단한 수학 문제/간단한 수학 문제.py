import copy, sys, math; sys.setrecursionlimit(100000)
N, K, X = map(int, input().split())
if K < 2*N-1: print(-1); exit()

def Combination_with_Repete(X, n, r):
    A = n+r-1
    r = min(A-r, r)
    neu, den = 1, 1
    for i in range(1, r+1):
        neu *= (A-i+1)
        den *= i
        gcd = math.gcd(neu, den)
        neu, den = neu // gcd, den // gcd
        if neu/den > X:
            return X+1
    return neu // den

M = (K-(2*N-1))//2
n = N
r = M-1

if Combination_with_Repete(X, N, M) < X: print(-1); exit()

Left, Mid = [], [N]
idx = 1

Array = [1]*(N+1)
Array[N], Array[0] = 0, 0
if not K % 2:
    Array[N] = 1
    Mid = []

while X > 0 and r >= 0 and idx <= N:
    if X > (C := Combination_with_Repete(X, n, r)):
        X -= C
        n -= 1
        idx += 1
    else:
        Array[idx] += 1
        r -= 1

for i in range(1, N+1):
    Left += [i]*Array[i]

Right = copy.deepcopy(Left)
Right.reverse()
Answer = Left + Mid + Right
print(*Answer)