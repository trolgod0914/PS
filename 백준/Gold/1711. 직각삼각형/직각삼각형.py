import sys; input = sys.stdin.readline
N = int(input())
Array = [tuple(map(int, input().split())) for _ in range(N)]
Answer = 0
for i in range(N-2):
    x1, y1 = Array[i]
    for j in range(i+1, N-1):
        x2, y2 = Array[j]
        D2 = (x1-x2)**2+(y1-y2)**2
        for k in range(j+1, N):
            x3, y3 = Array[k]
            D1 = (x1-x3)**2+(y1-y3)**2
            D3 = (x2-x3)**2+(y2-y3)**2
            if D1+D2+D3 == 2*max(D1, D2, D3): Answer += 1
print(Answer)