import sys, heapq; input = sys.stdin.readline
N = int(input())
Heap = []
Answer = []
for _ in range(N):
    w, d = map(int, input().split())
    heapq.heappush(Heap, (d, w))
while Heap:
    D, W = heapq.heappop(Heap)
    if len(Answer) < D:
        heapq.heappush(Answer, W)
    else:
        if W > Answer[0]:
            heapq.heappop(Answer)
            heapq.heappush(Answer, W)
print(sum(Answer))