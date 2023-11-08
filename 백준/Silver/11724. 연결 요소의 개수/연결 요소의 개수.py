import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Dict = {}
array = deque(list(x+1 for x in range(N)))

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
                Stack += List
    return Array

count = 0
while len(array) > 0:
    A = DFS(Dict, array.popleft())
    array = deque(list(set(array) - set(A)))
    count += 1

print(count)