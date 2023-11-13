import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Array = [list(input().rstrip()) for _____ in range(N)]
visited = [[[0 for _ in range(M)] for __ in range(N)] for ___ in range(2)]

def BFS():
    Queue = deque([(0, 0, 1, 1)])
    visited[0][0][0], visited[1][0][0] = 1, 1
    Answer = []
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y, z, k = Queue.popleft()
        if x == N-1 and y == M-1:
            Answer.append(z)
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[0][nx][ny] == 1:
                continue
            if k == 0 and visited[1][nx][ny] == 1:
                continue
            if Array[nx][ny] == '1':
                if k == 1:
                    Queue.append((nx, ny, z+1, 0))
                    visited[0][nx][ny] = 1
                    visited[1][nx][ny] = 1
                else:
                    continue
            if Array[nx][ny] == '0':
                if k == 1:
                    Queue.append((nx, ny, z+1, 1))
                    visited[0][nx][ny] = 1
                    visited[1][nx][ny] = 1
                else:
                    Queue.append((nx, ny, z+1, 0))
                    visited[1][nx][ny] = 1
    return Answer
if answer:= BFS():
    print(min(answer))
else:
    print(-1)