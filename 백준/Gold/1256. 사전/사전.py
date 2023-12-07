from math import *
N, M, K = map(int, input().split())
if K > comb(N+M, M):
    print(-1)
    exit()
Answer = ''
A, Z = 0, 0
i, j = N-1, M
while A < N and Z < M:
    C = comb(i+j, j)
    if C >= K:
        Answer += 'a'
        i -= 1
        A += 1
    else:
        Answer += 'z'
        j -= 1
        Z += 1
        K -= C

for _ in range(N-A):
    Answer += 'a'
for _ in range(M-Z):
    Answer += 'z'

print(Answer)