import sys; input = sys.stdin.readline
N = int(input())
House = [list(map(int, input().split())) for _ in range(N)]

def DFS():
    Stack = [(0, 0, 1)]
    Move = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]
    Answer = 0
    while Stack:
        w, x, y = Stack.pop()
        if x == N-1 and y == N-1: Answer += 1; continue
        for dx, dy, dw in Move[w]:
            nx, ny, nw = x+dx, y+dy, dw
            if nx < 0 or nx >= N or ny < 0 or ny >= N or House[nx][ny]: continue
            if nw == 2:
                if House[nx][ny-1] or House[nx-1][ny]: continue
            Stack.append((nw, nx, ny))
    return print(Answer)

DFS()