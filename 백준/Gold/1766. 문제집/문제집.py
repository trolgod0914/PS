import sys, heapq; input = sys.stdin.readline
N, M = map(int, input().split())
ID = [0 for _ in range(N+1)]
Order = [[] for _ in range(N+1)]
Heap = []
Answer = []
for _ in range(M):
    A, B = map(int, input().split())
    Order[A].append(B)
    ID[B] += 1
for i in range(1, N+1):
    if ID[i] == 0:
        heapq.heappush(Heap, i)
while Heap:
    check = heapq.heappop(Heap)
    Answer.append(check)
    for j in Order[check]:
        ID[j] -= 1
        if ID[j] == 0:
            heapq.heappush(Heap, j)
print(*Answer)