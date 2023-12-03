import sys
N = int(input())
COST = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e6+1)
memo_R = [(COST[0][0], COST[0][0], INF, INF, INF, INF)]
memo_G = [(INF, INF, COST[0][1], COST[0][1], INF, INF)]
memo_B = [(INF, INF, INF, INF, COST[0][2], COST[0][2])]

def Cost(N, memo):
    if N > 1 and len(memo) < N:
        r1, r2, g1, g2, b1, b2 = Cost(N-1, memo)
        R, G, B = COST[N-1]
        r, g, b = min(r1, r2), min(g1, g2), min(b1, b2)
        memo.append((g+R, b+R, r+G, b+G, r+B, g+B))
    return memo[N-1]

Red, Green, Blue = Cost(N-1, memo_R), Cost(N-1, memo_G), Cost(N-1, memo_B)
R, G, B = COST[N-1]
Rr, Rg, Rb = min(Red[0], Red[1]), min(Red[2], Red[3]), min(Red[4], Red[5])
Gr, Gg, Gb = min(Green[0], Green[1]), min(Green[2], Green[3]), min(Green[4], Green[5])
Br, Bg, Bb = min(Blue[0], Blue[1]), min(Blue[2], Blue[3]), min(Blue[4], Blue[5])
print(Answer := min(min(Rr + min(G, B), Rg + B, Rb + G), min(Gr + B, Gg + min(R, B), Gb + R), min(Br + G, Bg + R, Bb + min(R, G))))