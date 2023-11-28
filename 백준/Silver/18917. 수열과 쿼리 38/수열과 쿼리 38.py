import sys; input = sys.stdin.readline
from bisect import bisect_left
M = int(input())
Xor = 0
Sum = 0
for _ in range(M):
    Order = list(map(int, input().split()))
    if Order[0] == 1:
        Xor ^= Order[1]
        Sum += Order[1]
    if Order[0] == 2:
        Xor ^= Order[1]
        Sum -= Order[1]
    if Order[0] == 3:
        print(Sum)
    if Order[0] == 4:
        print(Xor)