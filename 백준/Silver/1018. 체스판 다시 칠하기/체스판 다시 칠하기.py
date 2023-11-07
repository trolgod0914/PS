import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Jimin = [10101010, 1010101]
Sum = 0
Answer = []
Array = []


for i in range(N):

    Array.append([])
    pattern = input().rstrip()
    A = []

    for j in pattern:
        if j == 'W':
            A.append('1')
        else:
            A.append('0')

    pattern = ''.join(A)
    
    for k in range(M-7):
        Time = 0
        if i % 2 == 0:
            Count = str(int(pattern[k:k+8]) + Jimin[0])
        else:
            Count = str(int(pattern[k:k+8]) + Jimin[1])
        for l in range(len(Count)):
            if Count[l] == '1':
                Time +=1
        Array[i].append(Time)

for x in range(M-7):
    for y in range(N-7):
        for z in range(y, y+8):
            Sum += Array[z][x]
        Answer.append(Sum)
        Sum = 0

for a in range(len(Answer)):
    if Answer[a] > 32:
        Answer[a] = 64 - Answer[a]

print(min(Answer))