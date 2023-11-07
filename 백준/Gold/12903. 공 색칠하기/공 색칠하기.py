import sys
input = sys.stdin.readline

memo = [1, 1, 2, 6]

def factorial(n):
    global memo
    for i in range(n):
        if n > 3 and len(memo) < n+1:
            memo.append(factorial(n-1) * n)
    return memo[n]

def Combination(N, K):
    return factorial(N)//factorial(K)//factorial(N-K)

def Permutation(N, K):
    return factorial(N)//factorial(N-K)

num = 0
answer = 1
T = int(input())
for i in range(T):
    N = int(input().rstrip())
    if i == 0:
        num += N
    else:
        num += N-1
        answer *= Combination(num, N-1)
        num += 1

print(answer%(10**9+7))