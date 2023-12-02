import sys, heapq; input = sys.stdin.readline

V, E = map(int, input().split())
Line = {x: [] for x in range(1, V+1)}

for _ in range(E):
    A, B, C = map(int, input().split())
    Line[A].append((C, B))
    Line[B].append((C, A))

def Prim():
    Sum_of_Weight = 0
    Heap = []
    heapq.heappush(Heap, (0, 1))
    check = set()
    while Heap:
        Weight, Vertex = heapq.heappop(Heap)
        if Vertex not in check:
            check.add(Vertex)
            Sum_of_Weight += Weight
            for w, v in Line[Vertex]:
                if v not in check:
                    heapq.heappush(Heap, (w, v))
    return Sum_of_Weight

print(Prim())