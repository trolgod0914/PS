from bisect import *
import sys; input = sys.stdin.readline

N = int(input())
Sequence = list(map(int, input().split()))
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

key = len(Array)-1
M = len(List)
Answer = []

for j in range(M-1, -1, -1):
    if List[j][1] == key:
        Answer.append(List[j][0])
        key -= 1
    if key == 0:
        break

print(len(Answer))
print(*Answer[::-1])