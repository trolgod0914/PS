import sys, heapq; input = sys.stdin.readline
N, M = map(int, input().split())
ID = [0 for _ in range(N+1)]
Order = [set() for _ in range(N+1)]
Heap = []

for _ in range(M):
    Array = list(map(int, input().split()))
    for i in range(1, Array[0]+1):
        for ii in range(i+1, Array[0]+1):
            if Array[ii] not in Order[Array[i]]:
                Order[Array[i]].add(Array[ii])
                ID[Array[ii]] += 1

Answer = []

for i in range(1, N+1):
    if ID[i] == 0:
        heapq.heappush(Heap, i)
while Heap:
    Answer.append(check := heapq.heappop(Heap))
    for j in Order[check]:
        ID[j] -= 1
        if ID[j] == 0:
            heapq.heappush(Heap, j)

if len(Answer) == N:
    for l in Answer:
        print(l)
else:
    print(0)