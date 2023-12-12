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

L = int(input())
S = input()
print(L-KMP(S))