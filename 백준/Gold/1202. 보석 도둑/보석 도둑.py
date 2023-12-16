import sys, heapq; input = sys.stdin.readline
N, K = map(int, input().split())
Jewel, Bag, List = [], [], []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(Jewel, (M, V))
for _ in range(K):
    Bag.append(int(input()))
Bag.sort()
Answer = 0
for C in Bag:
    while Jewel:
        m, v = heapq.heappop(Jewel)
        if m <= C:
            heapq.heappush(List, -v)
        else:
            heapq.heappush(Jewel, (m, v))
            break
    if List:
        Answer -= heapq.heappop(List)
print(Answer)