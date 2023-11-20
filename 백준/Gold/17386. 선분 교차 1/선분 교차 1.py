x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
B = x1*y2 + x2*y4 + x4*y1 - x2*y1 - x4*y2 - x1*y4
C = x3*y4 + x4*y1 + x1*y3 - x4*y3 - x1*y4 - x3*y1
D = x3*y4 + x4*y2 + x2*y3 - x4*y3 - x2*y4 - x3*y2

answer = 0
if A*B <= 0 and C*D <= 0:
    answer = 1

print(answer)