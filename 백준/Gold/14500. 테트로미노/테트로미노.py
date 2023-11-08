import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Array = [list(map(int, input().split())) for i in range(N)]
Sum = [0]
for j in range(N):
    for k in range(M):
        if j < N-3:
            S = Array[j][k] + Array[j+1][k] + Array[j+2][k] + Array[j+3][k]
            Sum.append(S)
        if k < M-3:
            S = Array[j][k] + Array[j][k+1] + Array[j][k+2] + Array[j][k+3]
            Sum.append(S)
        if j < N-2:
            S = Array[j][k] + Array[j+1][k] + Array[j+2][k]
            for x in [k-1, k+1]:
                if x < 0 or x >= M:
                    continue
                for y in range(j, j+3):
                    A = S + Array[y][x]
                    Sum.append(A)
        if k < M-2:
            S = Array[j][k] + Array[j][k+1] + Array[j][k+2]
            for x in [j-1, j+1]:
                if x < 0 or x >= N:
                    continue
                for y in range(k, k+3):
                    A = S + Array[x][y]
                    Sum.append(A)
        if k > 0 and k < M-1 and j < N-1:
            S = Array[j][k] + Array[j+1][k]
            A = S + Array[j][k+1] + Array[j+1][k-1]
            B = S + Array[j][k-1] + Array[j+1][k+1]
            Sum.append(A)
            Sum.append(B)
        if j > 0 and j < N-1 and k < M-1:
            S = Array[j][k] + Array[j][k+1]
            A = S + Array[j+1][k] + Array[j-1][k+1]
            B = S + Array[j-1][k] + Array[j+1][k+1]
            Sum.append(A)
            Sum.append(B)
        if j < N-1 and k < M-1:
            S = Array[j][k] + Array[j][k+1] + Array[j+1][k] + Array[j+1][k+1]
            Sum.append(S)
print(max(Sum))