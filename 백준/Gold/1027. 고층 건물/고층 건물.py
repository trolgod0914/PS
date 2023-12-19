import sys; input = sys.stdin.readline
N = int(input())
Array = list(map(int, input().split()))
List = []
for i in range(N):
    Answer = 0
    x1, y1 = i, Array[i]
    Left, Right = int(1e9), -int(1e9)
    for j in range(i, -1, -1):
        if i == j:
            continue
        x2, y2 = j, Array[j]
        if (C:=(y1-y2)/(x1-x2)) < Left:
            Left = C
            Answer += 1
    for k in range(i, N):
        if i == k:
            continue
        x3, y3 = k, Array[k]
        if (D:=(y3-y1)/(x3-x1)) > Right:
            Right = D
            Answer += 1
    List.append(Answer)
print(max(List))