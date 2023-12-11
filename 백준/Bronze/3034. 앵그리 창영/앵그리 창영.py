from math import *
N, W, H = map(int, input().split())
for _ in range(N):
    L = int(input())
    if L <= sqrt(W*W+H*H):
        print("DA")
    else:
        print("NE")