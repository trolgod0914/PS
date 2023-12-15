import sys, heapq; input = sys.stdin.readline
def solution():
    List = []
    Heap = []
    for _ in range(N:=int(input())):
        S, T = map(int, input().split())
        heapq.heappush(List, (S, T))
    s, t = heapq.heappop(List)
    heapq.heappush(Heap, t)
    while List:
        s, t = heapq.heappop(List)
        if s < Heap[0]:
            heapq.heappush(Heap, t)
        else:
            heapq.heappop(Heap)
            heapq.heappush(Heap, t)
    print(len(Heap))
solution()