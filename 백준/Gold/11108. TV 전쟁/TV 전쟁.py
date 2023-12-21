import sys; input = sys.stdin.readline
from collections import defaultdict
def solution():
    DP = [0]*10081
    Dict = defaultdict(list)
    for _ in range(int(input())):
        s, d, p = map(int, input().split())
        Dict[s+d].append((s, p))
    for i in range(1, 10081):
        for S, P in Dict[i]:
            if DP[i] < DP[S] + P:
                DP[i] = DP[S] + P
        DP[i] = max(DP[i-1], DP[i])
    return print(DP[-1])

for _ in range(int(input())):
    solution()