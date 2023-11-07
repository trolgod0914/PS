import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
def Supply(N, M, L):
    if M == 1:
        return N % L
    if M == 2:
        return (N * N) % L
    else:
        if M % 2 == 0:
            return (Supply(N, M//2, L) ** 2) % L
        else:
            return ((Supply(N, M//2, L) ** 2) * N) % L

print(Supply(A, B, C))