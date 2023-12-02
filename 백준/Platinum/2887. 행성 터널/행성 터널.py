import sys, heapq; input = sys.stdin.readline
X, Y, Z = [], [], []
INF = 3000000000
Line = {}
N = int(input())
for i in range(1, N+1):
    x, y, z = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))
Line = {x: [] for x in range(1, N+1)}
X.sort()
Y.sort()
Z.sort()
X = [(-INF, N+1)] + X + [(INF, N+2)]
Y = [(-INF, N+1)] + Y + [(INF, N+2)]
Z = [(-INF, N+1)] + Z + [(INF, N+2)]

for k in range(1, N+1):
    a, b = X[k]
    c, d = Y[k]
    e, f = Z[k]
    a1, b1 = X[k-1]
    a2, b2 = X[k+1]
    c1, d1 = Y[k-1]
    c2, d2 = Y[k+1]
    e1, f1 = Z[k-1]
    e2, f2 = Z[k+1]
    wa1, wa2, wc1, wc2, we1, we2 = abs(a-a1), abs(a-a2), abs(c-c1), abs(c-c2), abs(e-e1), abs(e-e2)
    if k == 1:
        Line[b].append((wa2, b2))
        Line[b2].append((wa2, b))
        Line[d].append((wc2, d2))
        Line[d2].append((wc2, d))
        Line[f].append((we2, f2))
        Line[f2].append((we2, f))
    elif k == N:
        Line[b].append((wa1, b1))
        Line[b1].append((wa1, b))
        Line[d].append((wc1, d1))
        Line[d1].append((wc1, d))
        Line[f].append((we1, f1))
        Line[f1].append((we1, f))
    else:
        Line[b].append((wa2, b2))
        Line[b2].append((wa2, b))
        Line[d].append((wc2, d2))
        Line[d2].append((wc2, d))
        Line[f].append((we2, f2))
        Line[f2].append((we2, f))
        Line[b].append((wa1, b1))
        Line[b1].append((wa1, b))
        Line[d].append((wc1, d1))
        Line[d1].append((wc1, d))
        Line[f].append((we1, f1))
        Line[f1].append((we1, f))

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