import sys, heapq; input = sys.stdin.readline
Heap = []
N = int(input())
for _ in range(N):
    heapq.heappush(Heap, int(input()))
Answer = 0
while len(Heap) > 1:
    A = heapq.heappop(Heap)
    B = heapq.heappop(Heap)
    C = A+B
    Answer += C
    heapq.heappush(Heap, C)
print(Answer)