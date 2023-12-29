import sys; input = sys.stdin.readline

def Bag():
    N, M = map(int, input().split())
    Memory = [0] + list(map(int, input().split()))
    Cost = [0] + list(map(int, input().split()))
    Min_Cost = 1000000
    C = sum(Cost)
    DP = [[0]*(C+1) for _ in range(N+1)]
    for idx in range(1, N+1):
        Cidx = Cost[idx]
        for c in range(C+1):
            if Cidx <= c: DP[idx][c] = max(DP[idx-1][c], DP[idx-1][c-Cidx] + Memory[idx])
            else: DP[idx][c] = DP[idx-1][c]
    for index in range(1, N+1):
        for cost in range(C+1):
            if DP[index][cost] >= M: Min_Cost = min(Min_Cost, cost); break
    return print(Min_Cost)

Bag()