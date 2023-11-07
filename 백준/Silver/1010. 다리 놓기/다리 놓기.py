def factorial(n):
    global memo
    for i in range(n):
        if n > 3 and len(memo) < n+1:
            memo.append(factorial(n-1) * n)
    return memo[n]
memo = [1, 1, 2, 6]
for i in range(int(input())):
    N, M = map(int, input().split())
    print(factorial(M)//factorial(N)//factorial(M-N))