from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Array = list(map(int, input().split()))
Array.sort()
answer = combinations_with_replacement(Array, M)
for i in answer:
    print(*i)