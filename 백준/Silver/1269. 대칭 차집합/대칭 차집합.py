import sys
input = sys.stdin.readline
N, M = map(int, input().split())
count = 0
Dict_A = {}
array_A = list(map(int, input().split()))
for a in array_A:
    Dict_A[a] = 1
Dict_B = {}
array_B = list(map(int, input().split()))
for b in array_B:
    Dict_B[b] = 1
for A in array_A:
    if A not in Dict_B:
        count += 1
for B in array_B:
    if B not in Dict_A:
        count += 1
print(count)