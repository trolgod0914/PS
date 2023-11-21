import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())

Information = [[] for _ in range(N+1)] # 그래프 생성

for _ in range(E):
    u, v, w = map(int, input().split())
    Information[u].append((v, w))
    Information[v].append((u, w)) # 도착점, 가중치 튜플로 저장 (양방향)

v1, v2 = map(int, input().split())
INF = int(1e9)

def solution(start, end):
    Queue = []
    heapq.heappush(Queue, (0, start)) # 우선순위, 값 형태로 들어간다.
    Standard = [INF] * (N+1) # 판단기준을 잡아준다.
    if start == end:
        Standard[start] = 0
    while Queue:
        cost, place = heapq.heappop(Queue)

        if Standard[place] < cost:
            continue

        for destination, weight in Information[place]:    
            if cost + weight < Standard[destination]: 
                Standard[destination] = cost + weight  
                heapq.heappush(Queue, (cost+weight, destination))
    return Standard[end]

one_to_v1 = solution(1, v1)
one_to_v2 = solution(1, v2)
v1_to_v2 = solution(v1, v2)
v2_to_v1 = solution(v2, v1)
v1_to_N = solution(v1, N)
v2_to_N = solution(v2, N)

if one_to_v1 != INF and v1_to_v2 != INF and v2_to_N != INF:
    Answer1 = one_to_v1 + v1_to_v2 + v2_to_N
else:
    Answer1 = -1

if one_to_v2 != INF and v2_to_v1 != INF and v1_to_N != INF:
    Answer2 = one_to_v2 + v2_to_v1 + v1_to_N
else:
    Answer2 = -1

if Answer1 + Answer2 < 0:
    print(-1)
elif Answer1 * Answer2 < 0:
    print(max(Answer1, Answer2))
else:
    print(min(Answer1, Answer2))