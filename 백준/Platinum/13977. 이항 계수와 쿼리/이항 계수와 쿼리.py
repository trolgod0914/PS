import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(1000000)

Mod = int(1e9+7)
C = 4 * int(1e6) + 1
Factorial = [1] * C

for i in range(1, C):
    Factorial[i] = Factorial[i-1] * i % Mod

def power(a, n):
    if n == 0:
        return 1
    x = power(a, n//2)
    if n % 2 == 0:
        return (x * x) % Mod
    else:
        return (x * x * a) % Mod

for _ in range(int(input())):
    N, K = map(int, input().split())
    Numerator = Factorial[N]
    Denoinator = Factorial[K] * Factorial[N-K] % Mod
    print(str(power(Denoinator, Mod-2) * Numerator % Mod) + '\n')