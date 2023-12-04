import sys; input = sys.stdin.readline
Stack = []
Max = 0
for i in range(N:=int(input())):
    num = int(input())
    while Stack and Stack[-1][0] > num:
        value, index = Stack.pop()
        if Stack:
            M = (i - Stack[-1][1] - 1) * value
        else:
            M = i * value
        if Max < M:
            Max = M
    Stack.append((num, i))

while Stack:
    value, index = Stack.pop()
    if Stack:
        M = (N - Stack[-1][1] - 1) * value
    else:
        M = N * value
    if Max < M:
        Max = M
print(Max)