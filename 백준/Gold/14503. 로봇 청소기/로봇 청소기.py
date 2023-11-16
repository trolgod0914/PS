def Robot_Vaccum(r, c, d, Room):
    Clean = 0
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while True:
        if Room[r][c] == 0:
            Room[r][c] = '1'
            Clean += 1
        else:
            if Room[r+1][c] != 0 and Room[r][c+1] != 0 and Room[r-1][c] != 0 and Room[r][c-1] != 0:
                dr, dc = move[(d+2)%4]
                nr, nc = r+dr, c+dc
                if Room[nr][nc] != 1:
                    r, c = nr, nc
                else:
                    break
            if Room[r+1][c] == 0 or Room[r][c+1] == 0 or Room[r-1][c] == 0 or Room[r][c-1] == 0:
                for _ in range(4):
                    d = (d-1)%4
                    dr, dc = move[d]
                    nr, nc = r+dr, c+dc
                    if Room[nr][nc] == 0:
                        r, c = nr, nc
                        break
    return Clean

N, M = map(int, input().split())
r, c, d = map(int, input().split())
Room = [list(map(int, input().split())) for _ in range(N)]
print(Robot_Vaccum(r, c, d, Room))