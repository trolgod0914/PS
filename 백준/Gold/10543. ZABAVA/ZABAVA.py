import sys; input = sys.stdin.readline
from collections import defaultdict

def Party(num, time):
    A, B = num//(time+1), num%(time+1)
    return (A*(A+1)*(time-B+1))//2+((A+1)*(A+2)*B)//2

N, M, K = map(int, input().split())
Array = [[0, 0] for _ in range(M+1)]
for _ in range(N):
    Array[int(input())][0] += 1

for _ in range(K):
    Key, Value = 0, 0
    for i in range(1, M+1):
        V, T = Array[i]
        Sol = Party(V, T) - Party(V, T+1)
        if Sol > Value: Key = i; Value = Sol
    Array[Key][1] += 1

Answer = 0

for j in range(1, M+1):
    Answer += Party(*Array[j])

print(Answer)