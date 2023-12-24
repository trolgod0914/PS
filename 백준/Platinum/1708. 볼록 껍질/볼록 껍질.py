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

def solution():
    Array = list(tuple(map(int, input().split())) for _ in range(int(input())))
    return print(len(Convex_Hull_Left_to_Right(Array) + Convex_Hull_Right_to_Left(Array)))

solution()