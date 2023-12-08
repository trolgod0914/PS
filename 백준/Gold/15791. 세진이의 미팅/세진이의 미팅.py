import sys, math
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
Mod = int(1e9+7)

def power(a, n):
    if n == 0:
        return 1
    x = power(a, n//2)
    if n % 2 == 0:
        return (x * x) % Mod
    else:
        return (x * x * a) % Mod

N1, N2 = 1, 1
K = N-M
for i in range(1, M+1):
    N1 *= (K+i)
    N2 *= i
    N1, N2 = N1%Mod, N2%Mod

print(str(power(N2, Mod-2) * N1 % Mod) + '\n')