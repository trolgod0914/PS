import sys

def LOS():
    N = int(input())
    Arr = list(map(int, sys.stdin.readline().split()))
    Sub = list(1 for i in range(N))
    for j in range(1, N):
        for k in range(0, j):
            if Arr[j] > Arr[k]:
                if Sub[k] + 1 > Sub[j]:
                    Sub[j] = Sub[k] + 1
    print(max(Sub))

LOS()