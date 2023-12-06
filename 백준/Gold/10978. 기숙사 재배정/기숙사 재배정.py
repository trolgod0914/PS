from math import *
memo = [0]*21
def RE(N):
    global memo
    if memo[N] != 0:
        return memo[N]
    Answer = 0
    for i in range(N+1):
        Answer += ((-1)**i) * comb(N, i) * perm(N-i, N-i)
    memo[N] = Answer
    return Answer

for _ in range(int(input())):
    print(RE(int(input())))