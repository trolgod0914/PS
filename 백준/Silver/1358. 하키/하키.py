import sys; input = sys.stdin.readline
W, H, X, Y, P = map(int, input().split())
Answer = 0
for _ in range(P):
    x, y = map(int, input().split())
    if (X <= x <= X+W and Y <= y <= Y+H) or (x-X)**2+(y-Y-H//2)**2 <= (H//2)**2 or (x-X-W)**2+(y-Y-H//2)**2 <= (H//2)**2: Answer += 1
print(Answer)