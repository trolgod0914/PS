import sys; input = sys.stdin.readline; print = sys.stdout.write

def CCW(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

def Distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(0.5)

def Weight(point, p):
    a, b = p
    x, y = point
    if y == b: return 0, Distance(p, point)
    if a < x: return 1, (y-b)/(x-a), Distance(p, point)
    if a == x: return 2, Distance(p, point)
    if a > x: return 3, (y-b)/(x-a), Distance(p, point)

def Convex_Hull(Array):
    Array.sort(key=lambda x:(x[1], x[0]))
    P = Array.pop(0)
    Array.sort(key=lambda x: Weight(x, P))
    Stack = [P]
    for point in Array:
        while len(Stack) >= 2 and CCW(Stack[-2], Stack[-1], point) <= 0: Stack.pop()    
        Stack.append(point)
    return Stack

def solution():
    Array = list(tuple(map(int, input().split())) for _ in range(int(input())))
    Answer = Convex_Hull(Array)
    Answer.append(Answer[0])
    Result = 0
    for i in range(len(Answer)-1):
        Result += Distance(Answer[i], Answer[i+1])
    return print('{:.2f}'.format(Result))

solution()