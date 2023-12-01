from bisect import *
import sys; input = sys.stdin.readline
N = int(input())
Line = {}
for _ in range(N):
    A, B = map(int, input().split())
    Line[B] = A
Line = dict(sorted(Line.items(), key=lambda item: item[1]))
Sequence = list(Line.keys())
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
delete = set()
answer = set()

for j in range(M-1, -1, -1):
    if List[j][1] == key:   
        delete.add(List[j][0])
        key -= 1
    if key == 0:
        break

for k in Sequence:
    if k not in delete:
        answer.add(Line[k])
print(len(answer))
for j in answer:
    print(j)