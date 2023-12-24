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
    N = int(input())
    M = N//5
    K = 1 if N%5 else 0
    Array = []
    for _ in range(M+K):
        Case = list(map(int, input().split()))
        for i in range(len(Case)//2): Array.append((Case[2*i], -Case[2*i+1]))
    Answer = Convex_Hull(Array)
    print(str(len(Answer))+'\n')
    for x, y in Answer: print('{} {}\n'.format(x, -y))

for _ in range(int(input())):
    solution()