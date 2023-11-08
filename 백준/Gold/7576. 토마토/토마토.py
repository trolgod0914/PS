import sys
from collections import deque
input = sys.stdin.readline

def BFS(array, List):
    Queue = deque(List)
    move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if array[nx][ny] == -1:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                Queue.append((nx, ny))
    return max([max(r) for r in array])-1

M, N = map(int, input().split())
array = [list(map(int, input().split())) for x in range(N)]
List = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 1:
            List.append((i, j))
result = (BFS(array, List))
for k in array:
    if 0 in k:
        result = -1
        break
print(result)