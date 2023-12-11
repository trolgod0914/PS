from bisect import bisect_left
P = int(input())
N = int(input())

DP = [[1, 0, 0]]
def Problem_solution(N):
    global DP
    if N > 1 and len(DP) < N:
        Array = Problem_solution(N-1)
        DP.append([Array[2], Array[0], Array[0]+Array[1]])
    return DP[N-1]
A = Problem_solution(N)
if P == 1:
    print(sum(A))

if P == 2:
    X1, X2, X3 = 'X', 'YZ', 'ZX'
    K = int(input())    
    while N > 3:
        if K > sum(DP[N-4]):
            K -= sum(DP[N-4])
            N -= 2
        else:
            N -= 3
    print([X1, X2, X3][N-1][K-1])
if P == 3:
    K = input()
    if K == 'X':
        M = 0
    elif K == 'Y':
        M = 1
    else:
        M = 2
    print(A[M])