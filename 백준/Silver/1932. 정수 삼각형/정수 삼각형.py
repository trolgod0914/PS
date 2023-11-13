import sys
N = int(input())
Array = [list(map(int, input().split())) for _ in range(N)]
Answer = [[0]*(i+1) for i in range(N)]
for j in range(N):
    for k in range(len(Array[j])):
        if j == 0:
            Answer[j][k] = Array[j][k]
        else:
            if k == 0:
                A = Answer[j-1][k]
            elif k == j:
                A = Answer[j-1][k-1]
            else:
                A = max(Answer[j-1][k-1], Answer[j-1][k])
            Answer[j][k] = A + Array[j][k]
print(max(Answer[N-1]))