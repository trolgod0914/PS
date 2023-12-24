import sys; input = sys.stdin.readline
N = int(input())
Array = list(map(int, input().split()))
if N == 1: print(Array[0]*4+2); exit()
if N == 2: print(Array[0]*4+2+Array[1]*4+2-2*min(Array[0], Array[1])); exit()
Answer = Array[-1]*4+2
for i in range(N-1):
    K = min(Array[i], Array[i+1])
    Answer += Array[i]*4+2-2*K
print(Answer)