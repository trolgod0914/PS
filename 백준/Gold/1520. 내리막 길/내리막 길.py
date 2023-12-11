import sys; input = sys.stdin.readline

M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1]*N for _ in range(M)]
def DFS(x, y):
    if x == M-1 and y == N-1:
        return 1
    if DP[x][y] > -1:
         return DP[x][y]
    DP[x][y] = 0
    Move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in Move:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and Map[nx][ny] < Map[x][y]:
                DP[x][y] += DFS(nx, ny)
    return DP[x][y]

print(DFS(0, 0))