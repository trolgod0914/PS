import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def power(a, n, l):
    if n == 0:
        return 1
    x = power(a, n//2, l)
    if n % 2 == 0:
        return (x * x) % l
    else:
        return (x * x * a) % l

M = int(input())
answer = 0
Mod = 1000000007
for _ in range(M):
    A, B = map(int, input().split())
    G = math.gcd(A, B)
    A, B == A//G, A//G
    answer += power(A, Mod-2, Mod) * B % Mod
    answer %= Mod
print(answer)