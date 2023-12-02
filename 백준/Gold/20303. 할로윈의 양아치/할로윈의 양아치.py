import sys; input = sys.stdin.readline
N, M, K = map(int, input().split())
Candy = [0] + list(map(int, input().split()))
Friend = [[] for _ in range(N+1)]
Check = [0 for _ in range(N+1)]
Information = [(0, 0)]
for _ in range(M):
    a, b = map(int, input().split())
    Friend[a].append(b)
    Friend[b].append(a)

def DFS(start):
    Stack = [start]
    candy = 0
    child = 0
    while Stack:
        num = Stack.pop()
        if not Check[num]:
            Check[num] = 1
            candy += Candy[num]
            child += 1
            Stack += Friend[num]
    return candy, child

for n in range(1, N+1):
    if not Check[n]:
        V, W = DFS(n)
        Information.append((W, V))

J = len(Information)-1
DP = [[0] * (K+1) for _ in range(J+1)]

def Bag(N, K, Information):
    for i in range(1, N+1):
        for j in range(1, K+1):
            if Information[i][0] <= j:
                DP[i][j] = max(Information[i][1] + DP[i-1][j-Information[i][0]], DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]
    return DP[N][K]

print(Bag(J, K-1, Information))