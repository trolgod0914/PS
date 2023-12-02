import sys, heapq, math; input = sys.stdin.readline
n = int(input())
Star = []
Line = {x: [] for x in range(1, n+1)}
for _ in range(n):
    A, B = map(float, input().split())
    Star.append((A, B))
for i in range(n-1):
    a, b = Star[i]
    for j in range(i, n):
        c, d = Star[j]
        W = math.pow(a-c, 2) + math.pow(b-d, 2)
        Line[i+1].append((W, j+1))
        Line[j+1].append((W, i+1))

def Prim():
    Sum_of_Weight = []
    Heap = []
    heapq.heappush(Heap, (0, 1))
    check = set()
    while Heap:
        Weight, Vertex = heapq.heappop(Heap)
        if Vertex not in check:
            check.add(Vertex)
            Sum_of_Weight.append(Weight)
            for w, v in Line[Vertex]:
                if v not in check:
                    heapq.heappush(Heap, (w, v))
    return Sum_of_Weight

Answer = 0
Sum = Prim()
for S in Sum:
    Answer += math.sqrt(S)
print(Answer)