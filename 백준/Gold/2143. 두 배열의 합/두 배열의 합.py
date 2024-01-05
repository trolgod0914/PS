import sys; input = sys.stdin.readline
from bisect import *

def Prefix_Sum(Array):
    List = [0]
    for i in range(len(Array)):
        List.append(List[i]+Array[i])
    return List

def Sum_of_Array(Prefix):
    Array = []
    for i in range(0, len(Prefix)-1):
        for j in range(i+1, len(Prefix)):
            Array.append(Prefix[j]-Prefix[i])
    Array.sort()
    return Array

T = int(input())
N = int(input())
An = list(map(int, input().split()))
M = int(input())
Bm = list(map(int, input().split()))
A = Sum_of_Array(Prefix_Sum(An))
B = Sum_of_Array(Prefix_Sum(Bm))

Answer = 0

for a in A:
    Answer += (bisect_right(B, T-a) - bisect_left(B, T-a))

print(Answer)