def factorial(n):
    global memo
    for i in range(n):
        if n > 3 and len(memo) < n+1:
            memo.append(factorial(n-1) * n)
    return memo[n]

N = int(input())
memo = [1, 1, 2, 6]
print(factorial(N))
