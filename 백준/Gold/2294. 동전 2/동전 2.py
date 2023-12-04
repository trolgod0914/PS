import sys; input = sys.stdin.readline
N, K = map(int, input().split())
Coin = []
for _ in range(N):
    Coin.append(int(input()))
Coin = list(set(Coin))
DP = [10001] * (K+1)
DP[0] = 0

for C in Coin:
    for k in range(1, K+1):
        if k-C >= 0:
            if DP[k-C] + 1 < DP[k]:
                DP[k] = DP[k-C] + 1

if DP[k] < 10001:
    print(DP[k])
else:
    print(-1)