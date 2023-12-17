import sys; input = sys.stdin.readline
from bisect import bisect_left
N, M = map(int, input().split())
Array = list(map(int, input().split()))
Array.sort()
idx = bisect_left(Array, 0)
Left, Right = Array[:idx], Array[idx:]
L, R = len(Left), len(Right)
Right.sort(reverse=True)
Answer = []
for i in range(0, L, M):
    Answer.append(-Left[i])
for j in range(0, R, M):
    Answer.append(Right[j])
Answer.sort()
K = Answer.pop()
print(2*sum(Answer)+K)