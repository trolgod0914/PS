import sys
input = sys.stdin.readline

def CaIn(x, y, M, N):
    key = x
    while key <= M*N:
        if (key-x) % M == 0 and (key-y) % N == 0:
            return key
        key += M
    return -1

for i in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(CaIn(x, y, M, N))