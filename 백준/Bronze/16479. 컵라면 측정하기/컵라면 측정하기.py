import sys, math; input = sys.stdin.readline
K = int(input())
D1, D2 = map(int, input().split())
if D1 == D2: print(K**2); exit()
L = abs(D1-D2)
print((4*K*K-L*L)/4)