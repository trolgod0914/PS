def KMP(target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    return Array[-1]

while True:
    S = input()
    if S == '.': exit()
    K = len(S)
    M = KMP(S)
    if K % (K-M):
        print(1)
    else:
        print(K//(K-M))