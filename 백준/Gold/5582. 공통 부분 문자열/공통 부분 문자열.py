String = input()
Sequence = input()
N, M = len(String), len(Sequence)
LCS = [[1]*(M+1) for _ in range(N+1)]
Max = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if String[i-1] == Sequence[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
for k in LCS:
    if max(k) > Max:
        Max = max(k)
print(Max-1)