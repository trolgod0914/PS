import sys; input = sys.stdin.readline
from collections import defaultdict

def find(x):
    if Array[x] != x:
        Array[x] = find(Array[x])
        return Array[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        Array[b] = a
    elif b < a:
        Array[a] = b

def CCW(x1, y1, x2, y2, x3, y3):
    A = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    if A > 0: return 1
    if A < 0: return -1
    return 0

def LSI(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    CCW12 = CCW(x1, y1, x2, y2, x3, y3)*CCW(x1, y1, x2, y2, x4, y4)
    CCW21 = CCW(x3, y3, x4, y4, x1, y1)*CCW(x3, y3, x4, y4, x2, y2)
    if CCW12 <= 0 and CCW21 <= 0:
        if CCW12 == 0 and CCW21 == 0:
            if max(x1, x2) < min(x3, x4): return False
            elif max(x3, x4) < min(x1, x2): return False
            elif max(y1, y2) < min(y3, y4): return False
            elif max(y3, y4) < min(y1, y2): return False
        return True
    return False

N = int(input())
Array = [x for x in range(N+1)]
List = [0] + [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1, N+1):
        if LSI(List[i], List[j]): union(i, j)

for i in range(1, N+1): Array[i] = find(Array[i])

Dict = defaultdict(int)
for i in range(1, N+1): Dict[Array[i]] += 1

Answer = list(Dict.values())

print(len(Answer))
print(max(Answer))