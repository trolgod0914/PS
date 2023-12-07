from math import *
N = int(input())
Array = [x for x in range(1, N+1)]
A = input()
if A[0] == '1':
    Answer = []
    B = int(A.split()[1])
    K = N-1
    while K > 0:
        d = factorial(K)
        C = (B-1) // d
        B = (B-1) % d + 1
        K -= 1
        M = Array[C]
        Answer.append(M)
        Array.remove(M)
    Answer += Array
    print(*Answer)
else:
    Answer = 1
    B = list(map(int, A.split()[1:]))
    K = N-1
    for i in B:
        Answer += Array.index(i) * factorial(K)
        Array.remove(i)
        K -= 1
    print(Answer)