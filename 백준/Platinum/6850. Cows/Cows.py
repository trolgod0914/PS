import sys; input = sys.stdin.readline

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)

def Convex_Hull_Left_to_Right(Array):
    List = sorted(Array)
    Left = []
    for point in List:
        while len(Left) >= 2:
            x1, y1 = Left[-2]
            x2, y2 = Left[-1]
            x3, y3 = point
            if CCW(x1, y1, x2, y2, x3, y3) > 0: break
            Left.pop()
        Left.append(point)
    return Left[:-1]

def Convex_Hull_Right_to_Left(Array):
    List = reversed(sorted(Array))
    Right = []
    for point in List:
        while len(Right) >= 2:
            x1, y1 = Right[-2]
            x2, y2 = Right[-1]
            x3, y3 = point
            if CCW(x1, y1, x2, y2, x3, y3) > 0: break
            Right.pop()
        Right.append(point)
    return Right[:-1]

def Convex_Hull():
    Array = list(tuple(map(int, input().split())) for _ in range(int(input())))
    return Convex_Hull_Left_to_Right(Array) + Convex_Hull_Right_to_Left(Array)

def Area(C1, C2):
    x1, y1 = C1
    x2, y2 = C2
    return (x1*y2 - x2*y1)

def solution():
    Coordinate = Convex_Hull()
    Coordinate.append(Coordinate[0])
    Answer = 0
    for i in range(0, len(Coordinate)-1):
        Answer += Area(Coordinate[i], Coordinate[i+1])
    return print(int(abs(Answer/100)))

solution()