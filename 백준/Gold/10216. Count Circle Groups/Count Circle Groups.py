import sys, math; input = sys.stdin.readline
from collections import defaultdict

def solution():
    Array = []
    Dict = defaultdict(list)
    for _ in range(N:=int(input())):
        Array.append(tuple(map(int, input().split())))
    for i in range(N-1):
        x1, y1, d1 = Array[i]
        for j in range(i+1, N):
            x2, y2, d2 = Array[j]
            r = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if d1 + d2 >= r:
                Dict[i].append(j)
                Dict[j].append(i)
    visited = [False]*N
    Answer = 0
    for i in range(N):
        if visited[i]:
            continue
        Answer += 1
        Stack = [i]
        while Stack:
            A = Stack.pop()
            visited[A] = True
            for B in Dict[A]:
                if not visited[B]:
                    Stack.append(B)
    return print(Answer)

for _ in range(int(input())):
    solution()