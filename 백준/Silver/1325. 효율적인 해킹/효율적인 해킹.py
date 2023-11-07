import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
dr = {x:[] for x in range(N+1)}

for i in range(M):
    A, B = map(int, input().split())
    if B not in dr:
        dr[B] = [A]
    else:
        dr[B].append(A)

def BFS(dictionary, root, array):
    queue = deque([root])
    array[root]=True
    count = 1
    while queue:
        n = queue.popleft()
        for w in dictionary[n]:
            if not array[w]:
                queue.append(w)
                array[w]=True
                count += 1
    return count
          
answer = {}
Max = 0
for j in range(1, N+1):
    visited = [False]*(N+1)
    value = BFS(dr, j, visited)
    if value >= Max:
        Max = value
        if value not in answer:
            answer[value] = [j]
        else:
            answer[value].append(j)

print(*answer[Max])