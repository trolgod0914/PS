import copy
from collections import deque

N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Wall = []
Virus = []

for a in range(N):
    for b in range(M):
        if Map[a][b] == 2:
            Virus.append((a, b))
            Map[a][b] = 1
        if Map[a][b] == 0:
            Wall.append((a, b))

def BFS(array):
    virus = copy.deepcopy(Virus)
    Queue = deque(virus)
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if array[nx][ny] == 1:
                continue
            if array[nx][ny] == 0:
                Queue.append((nx, ny))
                array[nx][ny] = 1
    Result = 0
    for i in array:
        Result += sum(i)
    return Result

key = len(Wall)
Answer = 0
for A in range(key-2):
    a1, b1 = Wall[A]
    for B in range(A+1, key-1):
        a2, b2 = Wall[B]
        for C in range(B+1, key):
            array = copy.deepcopy(Map)
            a3, b3 = Wall[C]
            array[a1][b1], array[a2][b2], array[a3][b3] = 1, 1, 1
            Sol = N*M - BFS(array)
            if Sol > Answer:
                Answer = Sol
print(Answer)