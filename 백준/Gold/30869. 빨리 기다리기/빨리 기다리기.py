import sys, heapq; input = sys.stdin.readline

N, M, K = map(int, input().split())
INF = int(1e7)
Information = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t, g = map(int, input().split())
    Information[s].append((e, t, g))


def solution():
    Queue = [(0, 1, 0)]
    Standard = [INF] * (N+1)
    Standard[1] = 0
    Max = INF
    while Queue:
        cost, place, Fastfowrad = heapq.heappop(Queue)

        if Standard[place] < cost:
            continue

        if place == N and cost < Max:
            Max = cost
            
        for destination, weight, wating in Information[place]:
            value = cost + weight + (wating-(cost%wating))%wating
            Value = cost + weight
            if value < Standard[destination]: 
                Standard[destination] = value
                heapq.heappush(Queue, (value, destination, Fastfowrad))
            if Fastfowrad < K and Value < Standard[destination] and Value < value:
                Standard[destination] = Value
                heapq.heappush(Queue, (Value, destination, Fastfowrad+1))

    if Max < INF:
        return Max
    else:
        return -1
    
print(solution())