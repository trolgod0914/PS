import sys, heapq; input = sys.stdin.readline
N = int(input())
Information = [[] for _ in range(N+1)]

for _ in range(M:=int(input())):
    a, b, c = map(int, input().split())
    Information[a].append((b, c))

INF = int(1e9)

def Floyd(start):
    Queue = []
    heapq.heappush(Queue, (0, start))
    Standard = [INF] * (N+1)
    Standard[start] = 0
    while Queue:
        cost, place = heapq.heappop(Queue)

        if Standard[place] < cost:
            continue

        for destination, weight in Information[place]:    
            if cost + weight < Standard[destination]: 
                Standard[destination] = cost + weight  
                heapq.heappush(Queue, (cost+weight, destination))
    
    for i in range(N+1):
        if Standard[i] == 1000000000:
            Standard[i] = 0
            
    return Standard[1:]

for j in range(N):
    print(*Floyd(j+1))