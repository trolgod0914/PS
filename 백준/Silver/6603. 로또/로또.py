import sys; input = sys.stdin.readline
from itertools import combinations as comb

Array = list(input().split())
if len(Array) > 1:
    K, Array = Array[0], Array[1:]
else:
    K = Array[0]

if K == '0': exit()
while True:
    List = list(comb(Array, 6))
    for a in List:
        print(' '.join(a))
    
    Array = list(input().split())
    if len(Array) > 1:
        K, Array = Array[0], Array[1:]
    else:
        K = Array[0]
    exit() if K == '0' else print()