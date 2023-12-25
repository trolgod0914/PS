import sys; input = sys.stdin.readline
from collections import deque
def Is_there_Cheese(Cheese, N, M):
    Sum = 0
    for i in range(N):
        Sum += sum(Cheese[i])
    return Sum

def BFS(Cheese, N, M):
    Queue = deque([(0, 0)])
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0]*M for _ in range(N)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if Cheese[nx][ny]: Cheese[nx][ny] += 1
                else: Queue.append((nx, ny)); visited[nx][ny] = 1

def Melting_Cheese(Cheese, N, M):
    for i in range(N):
        for j in range(M):
            if Cheese[i][j] == 2: Cheese[i][j] = 1
            if Cheese[i][j] >= 3: Cheese[i][j] = 0

def solution():
    N, M = map(int, input().split())
    Cheese = [list(map(int, input().split())) for _ in range(N)]
    Answer = 0
    while True:
        if not Is_there_Cheese(Cheese, N, M): return print(Answer)
        BFS(Cheese, N, M)
        Melting_Cheese(Cheese, N, M)
        Answer += 1

solution()