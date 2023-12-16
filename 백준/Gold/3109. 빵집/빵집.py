import sys; input = sys.stdin.readline
R, C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]

def DFS(r, c):
    Map[r][c] = 'X'
    move = [(-1, 1), (0, 1), (1, 1)]
    if c == C-1:
        return 1
    for dr, dc in move:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and Map[nr][nc] == '.':
            if DFS(nr, nc):
                return 1
    return 0
Answer = 0
for i in range(R):
    Answer += DFS(i, 0)
print(Answer)