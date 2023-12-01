Sequence1 = input()
Sequence2 = input()
N, M = len(Sequence1), len(Sequence2)
LCS = [[0]*(M+1) for _ in range(N+1)]
Max = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        LCS[i][j] = LCS[i-1][j]
    for j in range(1, M+1):
        if Sequence1[i-1] == Sequence2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

Y, X = N, M
Answer = ''
while X > 0 and Y > 0:
    if LCS[Y][X] == LCS[Y][X-1]:
        X -= 1
    elif LCS[Y-1][X] == LCS[Y][X]:
        Y -= 1
    else:
        Answer += Sequence2[X-1]
        X -= 1
        Y -= 1

Answer = ''.join(reversed(Answer))
print(LCS[N][M])
print(Answer)