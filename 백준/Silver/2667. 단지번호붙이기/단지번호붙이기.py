import sys
from collections import deque
input = sys.stdin.readline

def BFS(A, B):
    Queue = deque([(A, B)])
    List[A][B] = '0'
    Array = [1]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Queue:
        x, y = Queue.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if List[nx][ny] == '1':
                Queue.append((nx, ny))
                List[nx][ny] = '0'
                Array.append(1)
    return len(Array)

N = int(input())
List = [list(input().rstrip()) for i in range(N)]
Answer = []
for j in range(N):
    for k in range(N):
        if List[j][k] == '1':
            Answer.append(BFS(j, k))
Answer.sort()
print(len(Answer))
for l in Answer:
    print(l)