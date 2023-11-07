import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
Dict = {}

for i in range(M):
    A, B = map(int, input().split())
    if A not in Dict:
        Dict[A] = [B]
    elif B not in Dict[A]:
        Dict[A].append(B)
    if B not in Dict:
        Dict[B] = [A]
    elif A not in Dict[B]:
        Dict[B].append(A)

def DFS(Dictionary, Root):
    Array = []
    Stack = [Root]

    while Stack:
        n = Stack.pop()
        if n not in Array:
            Array.append(n)
            if n in Dict:
                List = list(set(Dict[n])-set(Array))
                List.sort(reverse=True)
                Stack += List
    return Array

def BFS(Dictionary, Root):
    Array = []
    Queue = deque([Root])

    while Queue:
        n = Queue.popleft()
        if n not in Array:
            Array.append(n)
            if n in Dict:
                List = list(set(Dict[n])-set(Array))
                List.sort()
                Queue += List
    return Array

print(*DFS(Dict, V))
print(*BFS(Dict, V))