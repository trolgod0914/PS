import sys; input = sys.stdin.readline

n = int(input())
Information = [[] for _ in range(n+1)]
for _ in range(n):
    Array = list(map(int, input().split()))
    for j in range(1, len(Array)//2):
        Information[Array[0]].append((Array[2*j-1], Array[2*j]))
        Information[Array[2*j-1]].append((Array[0], Array[2*j]))

def DFS(start):
    visited = set()
    visited.add(start)
    Diameter = [0] * (n+1)
    Stack = [start]
    Max, point = 0, 1
    while Stack:
        x = Stack.pop()
        for destination, weight in Information[x]:
            if destination not in visited:
                visited.add(destination)
                if Diameter[destination] < Diameter[x] + weight:
                    Diameter[destination] = Diameter[x] + weight
                if Diameter[destination] > Max:
                    Max, point = Diameter[destination], destination
                Stack.append(destination)
    return Max, point

print(DFS(DFS(1)[1])[0])