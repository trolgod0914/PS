import sys; input = sys.stdin.readline
N, M = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(N)]
Check = [[0]*M for _ in range(N)]
Direction = {'D': 0,
             'U': 1,
             'L': 2,
             'R': 3}
Move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def DFS(A, B, time):
    global answer
    Stack = [(A, B)]
    while Stack:
        x, y = Stack.pop()
        if Check[x][y]:
            if Check[x][y] == time:
                answer += 1
            return
        Check[x][y] = time
        dx, dy = Move[Direction[Map[x][y]]]
        nx, ny = x+dx, y+dy
        Stack.append((nx, ny))

answer = 0
time = 1
for A in range(N):
    for B in range(M):
        DFS(A, B, time)
        time += 1

print(answer)