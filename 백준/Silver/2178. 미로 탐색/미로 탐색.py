import sys
from collections import deque

def BFS(N, M, Array, List):
    Queue = deque([(0, 0, 1)])
    List[0][0] = 1
    move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while Queue:
        x, y, count = Queue.popleft()
        if (x, y) == (N-2, M-1) or (x, y) == (N-1, M-2):
            return count+1
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if Array[nx][ny] == '1' and List[nx][ny] == 0:
                Queue.append((nx, ny, count+1))
                List[nx][ny] = 1
N, M = map(int, input().split())
array = []
visited = [[0 for a in range(M)] for b in range(N)]
for j in range(N):
    array.append(list((input().rstrip())))
print(BFS(N, M, array, visited))