import sys; input = sys.stdin.readline
N, j, k = map(int, input().split())
a, b, c = j, j+k, j+k+k
Array = list(map(int, input().split()))
K = len(Array)
Array += [0, 0]
Answer = 0
if j <= k:
    for i in range(K):
        while Array[i] > 0:
            A = Array[i]
            Array[i] = 0
            Answer += A*a
else:
    for i in range(K):
        while Array[i] > 0:
            if Array[i+1] > Array[i+2]:
                A = min(Array[i], Array[i+1]-Array[i+2])
                Array[i] -= A
                Array[i+1] -= A
                Answer += b*A
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
                Answer += a*C + b*B + c*A
print(Answer)