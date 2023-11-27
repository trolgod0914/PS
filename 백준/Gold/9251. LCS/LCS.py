Sequence_1 = input()
Sequence_2 = input()
N, M = len(Sequence_1), len(Sequence_2)
LCS = [[0]*(M+1) for _ in range(N+1)]
Max = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if Sequence_1[i-1] == Sequence_2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
for k in LCS:
    if max(k) > Max:
        Max = max(k)
print(Max)