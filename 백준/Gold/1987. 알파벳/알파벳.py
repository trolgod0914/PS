R, C = map(int, input().split())
Array = [list(input()) for _ in range(R)]
def BFS():
    Queue = set([(0, 0, Array[0][0])])
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 1
    while Queue:
        x, y, v = Queue.pop()
        answer = max(answer, len(v))
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < R and 0 <= ny < C and Array[nx][ny] not in v:
                Queue.add((nx, ny, v+Array[nx][ny]))
    return answer
print(BFS())