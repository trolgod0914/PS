import sys; input = sys.stdin.readline
def solution():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2+(y1-y2)**2)**(0.5)
    if d == 0 and r1 == r2: return print(-1)
    if d > r1 + r2 or d < abs(r1 - r2): return print(0)
    if d == r1 + r2 or d == abs(r1 - r2): return print(1)
    if d < r1 + r2 or d > abs(r1 - r2): return print(2)
for _ in range(int(input())):
    solution()