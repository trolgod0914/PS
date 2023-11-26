import sys, copy; input = sys.stdin.readline; sys.setrecursionlimit(10000)
R, C, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]

def Air_Cleaner(Top, Bottom, map):
    # 공기 청정기 윗부분
    for down in range(Top-2, -1, -1):
        map[down+1][0] = map[down][0]
    for left in range(1, C):
        map[0][left-1] = map[0][left]
    for up in range(1, Top+1):
        map[up-1][C-1] = map[up][C-1]
    for right in range(C-2, 0, -1):
        map[Top][right+1] = map[Top][right]
    map[Top][1] = 0
    # 공기 청정기 아랫부분
    for up in range(Bottom+2, R):
        map[up-1][0] = map[up][0]
    for left in range(1, C):
        map[R-1][left-1] = map[R-1][left]
    for down in range(R-2, Bottom-1, -1):
        map[down+1][-1] = map[down][-1]
    for right in range(C-2, 0, -1):
        map[Bottom][right+1] = map[Bottom][right]
    map[Bottom][1] = 0

AirCleaner = []
for i in range(R):
    if Map[i][0] == -1: AirCleaner.append(i)
Top, Bottom = AirCleaner[0], AirCleaner[1]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    map = copy.deepcopy(Map)
    for a in range(R):
        for b in range(C):
            K = Map[a][b] // 5
            if K <= 0:
                continue
            for da, db in move:
                na, nb = a + da, b + db
                if 0 <= na < R and 0 <= nb < C and Map[na][nb] >= 0:
                    map[na][nb] += K
                    map[a][b] -= K
    Air_Cleaner(Top, Bottom, map)
    Map = copy.deepcopy(map)
    
Answer = 2
for Line in Map:
    Answer += sum(Line)

print(Answer)