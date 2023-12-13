import sys; input = sys.stdin.readline

def KMP(original, target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    Answer = []
    index = 0
    for j in range(len(original)):
        while index > 0 and target[index] != original[j]:
            index = Array[index-1]
        if target[index] == original[j]:
            index += 1
            if index == l:
                Answer.append(j-index+1)
                index = Array[index-1]
    return Answer

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = [0] * 360000
b = [0] * 360000
for i in range(N):
    a[A[i]] = 1
    b[B[i]] = 1
a = a+a
if KMP(a, b):
    print('possible')
else:
    print('impossible')