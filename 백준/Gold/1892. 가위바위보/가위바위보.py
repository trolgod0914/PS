import math
memo = [1, 1, 2, 6]

def factorial(n):
    global memo
    for i in range(n):
        if n > 3 and len(memo) < n+1:
            memo.append(factorial(n-1) * n)
    return memo[n]

def Sum_Fraction (A, B, C, D):
    E, F = A*D+B*C, B*D
    G = math.gcd(E, F)
    E, F = E//G, F//G
    return E, F

def Combination(N, K):
    return factorial(N)//factorial(K)//factorial(N-K)

def RSP(N, K):
    a, b = 0, 1
    for i in range(1, N+1):
        if i < K:
            continue
        if i >= K and i < 2*K-1:
            num_1, num_2 = Combination(i-1, K-1)*(2**(i-K)), 3**i
        if i >= 2*K-1:
            num = 0
            for j in range(i-2*K+1, i-K+1):
                num += factorial(i-1)//(factorial(K-1)*factorial(j)*factorial(i-K-j))
            num_1, num_2 = num, 3**i
        a, b = Sum_Fraction(a, b, num_1, num_2)
    return a, b

A, B = map(int, input().split())
a, b = RSP(A, B)
print(a, b)