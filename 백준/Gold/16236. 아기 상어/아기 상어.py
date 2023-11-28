import sys; input = sys.stdin.readline
from collections import deque
N = int(input())
Space = [list(map(int, input().split())) for _ in range(N)]
Fish = [0, 0, 0, 0, 0, 0, 0]
size = 2

for a in range(N):
    for b in range(N):
        if 1 <= Space[a][b] <= 6:
            Fish[Space[a][b]] += 1
        if Space[a][b] == 9:
            Shark_x, Shark_y = a, b
            Space[a][b] = 0

def DuruDuru(start_x, start_y, size):
    visited = [[0] * N for _ in range(N)]
    Queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 1
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    Array = [(1000, 0, 0, 0)]
    while Queue:
        x, y, d = Queue.popleft()
        if 0 < Space[x][y] < size:
            Array.append([d, x, y, Space[x][y]])
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and Space[nx][ny] <= size and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Queue.append((nx, ny, d+1))
    Array.sort(key=lambda x: x[2])
    Array.sort(key=lambda x: x[1])
    Array.sort(key=lambda x: x[0])
    return Array[0]

Answer = 0
Food = 0

while sum(Fish) and sum(Fish[:size]):
    List = DuruDuru(Shark_x, Shark_y, size)
    if List[0] > 999:
        break
    Answer += List[0]
    Shark_x, Shark_y, fish = List[1], List[2], List[3]
    Space[Shark_x][Shark_y] = 0
    Fish[fish] -= 1
    Food += 1
    if Food == size and size <= 6:
        Food, size = 0, size+1

print(Answer)