import sys; input = sys.stdin.readline
R, C, M = map(int, input().split())
Map = [[[]]*(C+1) for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    Map[r][c] = [r, c, s, d, z]

def Move(shark, next_map):
    r, c, s, d, z = shark
    S = s

    # 상어 움직이기
    while s:
        if d == 1:
            r -= (dr := min((r-1), s))
            s -= dr
            if s: d = 2
        elif d == 2:
            r += (dr := min((R-r), s))
            s -= dr
            if s: d = 1
        elif d == 3:
            c += (dc := min((C-c), s))
            s -= dc
            if s: d = 4
        else:
            c -= (dc := min((c-1), s))
            s -= dc
            if s: d = 3

    # 같은 공간에 상어가 있으면 잡아먹기
    if next_map[r][c]:
        if next_map[r][c][-1] < z: next_map[r][c] = [r, c, S, d, z]
    else:
        next_map[r][c] = [r, c, S, d, z]

    return next_map

def Fishing(column, Map):
    global Answer
    for i in range(1, R+1):
        if Map[i][column]: Answer += Map[i][column][-1]; Map[i][column] = []; break
    return Map

column = 1
Answer = 0
while column <= C:
    Map = Fishing(column, Map)
    next_map = [[[]]*(C+1) for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            if Map[i][j]: Move(Map[i][j], next_map)
    Map = next_map
    column += 1
print(Answer)