import sys; input = sys.stdin.readline
N, K = map(int, input().split())
Coin = []
for _ in range(N):
    Coin.append(int(input()))
DP = [0] * (K+1)
DP[0] = 1

for C in Coin:
    for k in range(1, K+1):
        if k-C >= 0:
            DP[k] += DP[k-C]
print(DP[K])