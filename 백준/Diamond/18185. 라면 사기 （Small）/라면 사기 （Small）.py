import sys; input = sys.stdin.readline
N = int(input())
Array = list(map(int, input().split()))
K = len(Array)
Array += [0, 0]
Answer = 0

for i in range(K):
    while Array[i] > 0:
        if Array[i+1] > Array[i+2]:
            A = min(Array[i], Array[i+1]-Array[i+2])
            Array[i] -= A
            Array[i+1] -= A
            Answer += 5*A
        else:
            A = min(Array[i], Array[i+1], Array[i+2])
            Array[i] -= A
            Array[i+1] -= A
            Array[i+2] -= A
            B = min(Array[i], Array[i+1])
            Array[i] -= B
            Array[i+1] -= B
            C = Array[i]
            Array[i] = 0
            Answer += 3*C + 5*B + 7*A
print(Answer)