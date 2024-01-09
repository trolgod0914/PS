import sys; input = sys.stdin.readline
from collections import deque

# 문과 열쇠 매칭
Door = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
        'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
        'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
        'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
Move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def Document(Map, Key_Check, H, W):

    # 방문체크 및 대기열
    visited = [[0]*(W) for _ in range(H)]
    Waiting = {x: [] for x in 'abcdefghijklmnopqrstuvwxyz'}

    Queue = deque([(0, 0)])
    Count = 0

    #BFS로 문서 찾기
    while Queue:
        r, c = Queue.popleft()
        for dr, dc in Move:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                Info = Map[nr][nc]

                # 벽을 만났다면 가지 않는다.
                if Info == '*': continue

                # 문서함이면 문서를 가지고, 카운트를 올린다.
                elif Info == '$':
                    Map[nr][nc] = '.'
                    Count += 1
                    Queue.append((nr, nc))

                # 열쇠를 찾았다면 열쇠를 가지고, 해당 열쇠를 기다리는 곳이 있다면 큐에 추가한다.
                elif Info in 'abcdefghijklmnopqrstuvwxyz':
                    Key_Check[Info] = True
                    Map[nr][nc] = '.'
                    Queue.append((nr, nc))
                    for i in Waiting[Info]:
                        Queue.append(i)

                # 문을 만났을 때 키가 있다면 지나가고, 아니면 기다린다.
                elif Info in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if Key_Check[Door[Info]]: Queue.append((nr, nc))
                    else: Waiting[Door[Info]].append((nr, nc))

                else: Queue.append((nr, nc))

                # 방문 여부를 기록한다.
                visited[nr][nc] = 1
    
    return Count


def solution():
    h, w = map(int, input().split())
    H, W = h+2, w+2

    # 지도 만들기
    Map = []
    Map.append(['.']*(W))
    for _ in range(h): Map.append(['.'] + list(input().rstrip()) + ['.'])
    Map.append(['.']*(W))

    # 열쇠 꾸러미 형성
    Key_Check = {x: False for x in 'abcdefghijklmnopqrstuvwxyz'}
    for key in input().rstrip(): Key_Check[key] = True

    return Document(Map, Key_Check, H, W)

for _ in range(int(input())):
    print(solution())