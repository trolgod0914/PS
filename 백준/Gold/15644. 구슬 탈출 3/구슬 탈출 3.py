import sys; input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
Board = [list(input().rstrip()) for _ in range(N)]
visited = {}
Move_Order = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
Key = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
for i in range(N):
    for j in range(M):
        K = Board[i][j]
        if K == 'R':
            r1, r2 = i, j
            Board[i][j] = '.'
        if K == 'B':
            b1, b2 = i, j
            Board[i][j] = '.'
        if K == 'O':
            ox, oy = i, j
            Board[i][j] = '.'

def Move(Order, rx, ry, bx, by):
    if Order == 'U':
        Stack = deque([(rx, ry, 'R'), (bx, by, 'B')]) if rx > bx else deque([(bx, by, 'B'), (rx, ry, 'R')])
    if Order == 'D':
        Stack = deque([(rx, ry, 'R'), (bx, by, 'B')]) if rx < bx else deque([(bx, by, 'B'), (rx, ry, 'R')])
    if Order == 'L':
        Stack = deque([(rx, ry, 'R'), (bx, by, 'B')]) if ry > by else deque([(bx, by, 'B'), (rx, ry, 'R')])
    if Order == 'R':
        Stack = deque([(rx, ry, 'R'), (bx, by, 'B')]) if ry < by else deque([(bx, by, 'B'), (rx, ry, 'R')])
    dx, dy = Move_Order[Order]
    r1, r2, b1, b2 = rx, ry, bx, by
    c = 0
    while Stack:
        x, y, Color = Stack.pop()
        if (x, y) == (ox, oy):
            if Color == 'R':
                c = -1
                r1, r2 = x, y
                continue
            else:
                c = 11
                b1, b2 = x, y
                break
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and Board[nx][ny] == '.':
            Stack.appendleft((nx, ny, Color))
        else:
            Board[x][y] = '#'
            if Color == 'R':
                r1, r2 = x, y
            else:
                b1, b2 = x, y
    Board[r1][r2] = '.'
    Board[b1][b2] = '.'   
    return r1, r2, b1, b2, c

def solution():
    Queue = deque([(r1, r2, b1, b2, '')])
    move = ['U', 'D', 'L', 'R']
    while Queue:
        R1, R2, B1, B2, T = Queue.popleft()
        if len(T) > 9: return -1
        for order in move:
            rx, ry, bx, by, c = Move(order, R1, R2, B1, B2)
            if c > 10: continue
            if c < 0: return T + order
            if (rx, ry, bx, by) not in visited:
                Queue.append((rx, ry, bx, by, T+order))
                visited[rx, ry, bx, by] = 0
    return -1

Answer = solution()
if Answer == -1:
    print(Answer)
else:
    print(len(Answer))
    print(Answer)