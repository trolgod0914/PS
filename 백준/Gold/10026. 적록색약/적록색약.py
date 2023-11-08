import sys, copy
from collections import deque
input = sys.stdin.readline

def BFS(Color, Array, a, b):
    Queue = deque([(a, b)])
    Array[a][b] = 0
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if Array[nx][ny] == Color:
                Queue.append((nx, ny))
                Array[nx][ny] = 0

def BFS_RG(Color, Array, a, b):
    Queue = deque([(a, b)])
    Array[a][b] = 0
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if Color == 'R' or Color == 'G':
                if Array[nx][ny] == 'R' or Array[nx][ny] == 'G':
                    Queue.append((nx, ny))
                    Array[nx][ny] = 0
            else:           
                if Array[nx][ny] == Color:
                    Queue.append((nx, ny))
                    Array[nx][ny] = 0
N = int(input())
List = [list(input().rstrip()) for i in range(N)]
array = copy.deepcopy(List)
count_0 = 0
count_1 = 0
for j in range(N):
    for k in range(N):
        key = array[j][k]
        if key != 0:
            BFS(key, array, j, k)
            count_0 +=1

for l in range(N):
    for m in range(N):
        key = List[l][m]
        if key != 0:
            BFS_RG(key, List, l, m)
            count_1 += 1

print(count_0, count_1)