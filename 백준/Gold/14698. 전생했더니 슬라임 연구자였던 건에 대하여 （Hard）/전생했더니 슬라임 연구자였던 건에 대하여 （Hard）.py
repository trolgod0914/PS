import sys, heapq; input = sys.stdin.readline
def solution():
    N = int(input())
    Mod = int(1e9+7)
    Array = list(map(int, input().split()))
    Array.sort()
    Answer = 1
    while len(Array) > 1:
        A = heapq.heappop(Array)
        B = heapq.heappop(Array)
        C = A*B
        Answer = (Answer*C)%Mod
        heapq.heappush(Array, C)
    return Answer
for _ in range(int(input())):
    print(solution())