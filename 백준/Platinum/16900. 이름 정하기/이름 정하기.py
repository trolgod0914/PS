def KMP(target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    return Array[l-1]

A, B = map(str, input().split())
C = len(A)
A = int(KMP(A))
B = int(B)
print(C+(B-1)*(C-A))