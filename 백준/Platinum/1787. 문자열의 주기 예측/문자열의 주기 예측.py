INF = int(1e9)

def KMP(target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    return Array

def Solution(num):
    global DP, Array
    if num < 0 or not Array[num]:
        return INF
    if DP[num] > -1:
        return DP[num]
    DP[num] = min(Array[num], Solution(Array[num]-1))
    return DP[num]

N = int(input())
S = input()
Array = KMP(S)
DP = [-1]*N
Answer = 0
for i in range(N):
    A = Solution(i)
    if A < INF:
        Answer += i + 1 - A 
print(Answer)