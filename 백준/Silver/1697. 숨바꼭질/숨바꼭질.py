import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0]*1000001

def BFS(num):
    time = 0
    Queue = deque([(num, time)])
    visited[num] = 1
    while Queue:
        x, t = Queue.popleft()
        if x == K:
            return t
        move = [x-1, x+1, x*2]
        for nx in move:
            if nx < 0 or nx > 1000000:
                continue
            if visited[nx] == 0:
                visited[nx] = 1
                Queue.append((nx, t+1))

print(BFS(N))