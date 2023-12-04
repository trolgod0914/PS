from bisect import *
import sys; input = sys.stdin.readline

N = int(input())
Sequence1 = list(map(int, input().split()))
Sequence2 = list(map(int, input().split()))
Sequence = []
Array = [0]*(N+1)

for n in range(N):
    Array[Sequence1[n]] = n

for num in Sequence2:
    Sequence.append(Array[num])

INF = int(1e9)
Array = [-INF]
List = [(-INF, 0)]
for i in range(0, N):
    if Sequence[i] > Array[-1]:
        Array.append(Sequence[i])
        List.append((Sequence[i], len(Array)-1))
    else:
        idx = bisect_left(Array, Sequence[i])
        Array[idx] = Sequence[i]
        List.append((Sequence[i], idx))

print(len(Array)-1)