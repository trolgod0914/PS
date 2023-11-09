import sys
input = sys.stdin.readline

N = int(input())
Array = list(map(str, input().split()))
for i in range(N-1, 0, -1):
    for j in range(i):
        Num_1 = Array[j]
        Num_2 = Array[j+1]
        Value_1 = int(Num_1 + Num_2)
        Value_2 = int(Num_2 + Num_1)
        if Value_1 < Value_2:
            Array[j], Array[j+1] = Array[j+1], Array[j]

Answer = ''.join(Array)
print(int(Answer))