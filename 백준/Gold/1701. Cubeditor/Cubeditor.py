import sys; sys.setrecursionlimit(10000)
def KMP(target):
    Array = [0] * (l:=len(target))
    idx = 0
    for i in range(1, l):
        while idx > 0 and target[idx] != target[i]:
            idx = Array[idx-1]
        if target[idx] == target[i]:
            idx += 1
            Array[i] = idx
    return max(Array)

S = input()
Answer = 0
for i in range(len(S)):
    String = S[i:]
    if (A:=KMP(String)) > Answer:
        Answer = A
print(Answer)