import sys
N = int(input())
COST = [list(map(int, input().split())) for _ in range(N)]

memo = [(COST[0][0], COST[0][0], COST[0][1], COST[0][1], COST[0][2], COST[0][2])]

def Cost(N):
    global memo
    if N > 1 and len(memo) < N:
        r1, r2, g1, g2, b1, b2 = Cost(N-1)
        [R, G, B] = COST[N-1]
        r, g, b = min(r1, r2), min(g1, g2), min(b1, b2)
        memo.append((g+R, b+R, r+G, b+G, r+B, g+B))
    return memo[N-1]

Answer = Cost(N)
print(min(Answer))