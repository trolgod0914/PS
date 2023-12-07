import sys; sys.setrecursionlimit(1000000)
memo = [0, 1]
Mod = int(1e9)
def derangement(N):
    global memo
    if N > 2 and len(memo) < N:
        memo.append((derangement(N-1)*N + (-1)**(N%2)) % Mod)
    return memo[N-1]

print(derangement(int(input())))