N = int(input())
Answer = 0
def Back_Tracking(x):
    global Answer
    Stack = [(x, 0, [x], [x], [x])]
    while Stack:
        x, y, x_line, upward, downward = Stack.pop()
        if y == N-1:
            Answer += 1
            continue
        for i in range(N):
            dx, dy = i, y+1
            A, B = dx+dy, dx-dy
            if dx in x_line:
                continue
            if A in upward:
                continue
            if B in downward:
                continue
            Stack.append((dx, dy, x_line + [dx], upward + [A], downward + [B]))

for X in range(N):
    Back_Tracking(X)

print(Answer)