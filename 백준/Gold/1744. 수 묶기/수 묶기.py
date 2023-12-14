import sys, heapq; input = sys.stdin.readline
Heap = []
Answer = 0
for _ in range(int(input())):
    heapq.heappush(Heap, -int(input()))
while len(Heap) > 1:
    A = -heapq.heappop(Heap)
    B = -heapq.heappop(Heap)
    if (C := A*B) > A:
        if A > 0:
            Answer += C
        else:
            if len(Heap)%2:
                heapq.heappush(Heap, -B)
                Answer += A
            else:
                Answer += C
    else:
        if not A:
            if not B:
                heapq.heappush(Heap, -B)
            else:
                if len(Heap)%2:
                    heapq.heappush(Heap, -B)
                else:
                    Answer += C
        else:
            Answer += A
            heapq.heappush(Heap, -B)
if Heap:
    Answer -= Heap.pop()
print(Answer)