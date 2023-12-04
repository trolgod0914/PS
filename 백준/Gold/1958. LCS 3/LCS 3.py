import sys; sys.setrecursionlimit(100000)

def LCS_Length():
    Sequence1 = input()
    Sequence2 = input()
    Sequence3 = input()
    N, M, K = len(Sequence1), len(Sequence2), len(Sequence3)
    LCS = [[[0]*(K+1) for _ in range(M+1)] for _ in range(N+1)]
    Max = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(1, K+1):
                if Sequence1[i-1] == Sequence2[j-1] and Sequence2[j-1] == Sequence3[k-1]:
                    LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
                else:
                    LCS[i][j][k] = max(LCS[i][j][k-1], LCS[i][j-1][k], LCS[i-1][j][k])
    print(LCS[N][M][K])
LCS_Length()