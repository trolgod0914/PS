import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = [[0]*N for _ in range(N)]
for i in range(N):
    K[i][i] = 1

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col))%1000 for B_col in zip(*B)] for A_row in A]

def Supply(A, B):
    if B == 1:
        return productMatrix(A, K)
    if B == 2:
        return productMatrix(A, A)
    else:
        C = Supply(A, B//2)
        D = productMatrix(C, C)
        if B % 2 == 0:
            return D
        else:
            return productMatrix(D, A)

Answer = Supply(A, B)
for i in Answer:
    print(*i)