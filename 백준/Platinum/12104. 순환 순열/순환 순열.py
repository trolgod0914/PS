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

A = input().rstrip()
B = input().rstrip()
b = B+B
b = b[:-1]
Answer = KMP(b, A)
print(len(Answer))