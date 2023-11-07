import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
Array = [x for x in range(1, N+1)]
Answer = []

while len(Array) > 1:

    if len(Array) < K:
        Array = Array * (K//len(Array) + 1)

    Minus = Array[K-1]
    Answer.append(Minus)
    Left_Side = Array[:K-1]
    while Minus in Left_Side:
        Left_Side.remove(Minus)
    Right_Side = Array[K:]
    while Minus in Right_Side:
        Right_Side.remove(Minus)
    Array = Right_Side + Left_Side

Answer += Array

print('<')
for i in Answer:
    if Answer[-1] == i:
        print(str(i))
    else:
        print(str(i) + ',' + ' ')
print('>')