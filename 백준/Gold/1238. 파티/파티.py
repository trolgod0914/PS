import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

Information = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    Information[u].append((v, w))
INF = int(1e9)

def solution_X(start):
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
    return Standard

def solution_N(start):
    Queue = []
    heapq.heappush(Queue, (0, start))
    Standard = [INF] * (N+1)
    Standard[start] = 0
    while Queue:
        cost, place = heapq.heappop(Queue)

        if place == X:
            return cost

        if Standard[place] < cost:
            continue

        for destination, weight in Information[place]:    
            if cost + weight < Standard[destination]: 
                Standard[destination] = cost + weight  
                heapq.heappush(Queue, (cost+weight, destination))

Answer = []
X_to_N = solution_X(X)
for num in range(1, N+1):
    Answer.append(X_to_N[num] + solution_N(num))
print(max(Answer))