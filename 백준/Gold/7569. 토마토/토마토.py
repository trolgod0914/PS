import sys
from collections import deque
input = sys.stdin.readline

def BFS(array, List):
    Queue = deque(List)
    answer = [0]
    move = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    while Queue:
        x, y, z = Queue.popleft()
        key = array[x][y][z]
        for dx, dy, dz in move:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz <0 or nz >= M:
                continue
            if array[nx][ny][nz] == -1:
                continue
            if array[nx][ny][nz] == 0:
                array[nx][ny][nz] = key+1
                answer.append(key)
                Queue.append((nx, ny, nz))
    return max(answer)

M, N, H = map(int, input().split())
array = [[list(map(int, input().split())) for x in range(N)] for y in range(H)]
List = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if array[i][j][k] == 1:
                List.append((i, j, k))
result = (BFS(array, List))
for l in range(H):
    for m in array[l]:
        if 0 in m:
            result = -1
            break
print(result)