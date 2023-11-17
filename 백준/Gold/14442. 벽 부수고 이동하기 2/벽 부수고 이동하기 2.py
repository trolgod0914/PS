import sys
from collections import deque
input = sys.stdin.readline

N, M, K  = map(int, input().split())
Array = [list(input().rstrip()) for _____ in range(N)]
visited = [[[0] * (K+1) for __ in range(M)] for ___ in range(N)]

def BFS():
    Queue = deque([(0, 0, 1, K)])
    visited[0][0][K] = 1
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y, z, k = Queue.popleft()
        if x == N-1 and y == M-1:
            return z
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][k] == 0:
                if Array[nx][ny] == '1':
                    if k >= 1:
                        if visited[nx][ny][k-1] == 1:
                            continue
                        Queue.append((nx, ny, z+1, k-1))
                        visited[nx][ny][k-1] = 1
                if Array[nx][ny] == '0':
                    Queue.append((nx, ny, z+1, k))
                    visited[nx][ny][k] = 1
    return -1
print(BFS())