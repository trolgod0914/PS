import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1]*1000001
Way = deque([])
def BFS(num):
    Queue = deque([(num, 0)])
    visited[num] = num
    while Queue:
        x, t = Queue.popleft()
        if x == K:
            Node = K
            while Node != num:
                Way.appendleft(Node)
                Node = visited[Node]
            Way.appendleft(Node)
            return t
        move = [x-1, x+1, x*2]
        for nx in move:
            if 0 <= nx < 1000001 and visited[nx] == -1:
                visited[nx] = x
                Queue.append((nx, t+1))
print(BFS(N))
print(*Way)