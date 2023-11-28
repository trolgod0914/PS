import sys
sys.setrecursionlimit(10000)
memo = {0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3}
mod = int(1000000)
def fibonacci(N):
    global memo
    if N not in memo:
        if N%2 == 0:
            memo[N] = ((fibonacci(N//2 + 1)**2) - (fibonacci(N//2 - 1)**2))%mod
        else:
            memo[N] = ((fibonacci(N//2 + 1)**2) + (fibonacci(N//2)**2))%mod
    return memo[N]
print(fibonacci(int(input())))