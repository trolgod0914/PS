import sys; input = sys.stdin.readline

Coordinate = []
Answer = 0

for _ in range(N := int(input())):
    x, y = map(int, input().split())
    Coordinate.append((x, y))

Coordinate.append(Coordinate[0])

def Area(C1, C2):
    x1, y1 = C1
    x2, y2 = C2
    return (x1*y2 - x2*y1)

for i in range(0, N):
    Answer += Area(Coordinate[i], Coordinate[i+1])

print(abs(Answer/2))