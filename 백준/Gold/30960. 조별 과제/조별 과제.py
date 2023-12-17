import sys; input = sys.stdin.readline
N = int(input())
Array = list(map(int, input().split()))
Array.sort()
if N == 3: print(Array[-1] - Array[0]); exit()
Duo, Trio = Array[1]-Array[0], Array[2]-Array[0]
for i in range(3, N, 2):
    Trio = min(Duo + Array[i+1] - Array[i-1], Trio + Array[i+1] - Array[i])
    Duo += Array[i]-Array[i-1]
print(Trio)