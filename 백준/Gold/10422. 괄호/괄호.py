import sys; sys.setrecursionlimit(1000000)
memo = [1, 1, 2, 5]
Mod = int(1e9+7)
def solution(N):
    global memo, Mod
    if N > 3 and len(memo) < N+1:
        S = 0
        for i in range(N):
            S += solution(i) * solution(N-1-i)
        memo.append(S % Mod)
    return memo[N]

for _ in range(int(input())):
    A = int(input())
    if A % 2:
        print(0)
    else:
        print(solution(A//2))