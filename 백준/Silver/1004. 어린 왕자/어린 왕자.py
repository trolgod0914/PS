import sys; input = sys.stdin.readline

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    Answer = 0
    for _ in range(int(input())):
        Cx, Cy, r = map(int, input().split())
        if ((Cx-x1)**2+(Cy-y1)**2-r**2) * ((Cx-x2)**2+(Cy-y2)**2-r**2) < 0:
            Answer += 1
    return print(Answer)

for _ in range(int(input())):
    solution()