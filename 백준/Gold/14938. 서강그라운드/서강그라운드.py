import sys, heapq; input = sys.stdin.readline; sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())
Items = [0] + list(map(int, input().split()))
Information = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    Information[a].append((b, l))
    Information[b].append((a, l))

INF = int(1e9)

def solution(start):
    Queue = []
    heapq.heappush(Queue, (0, start))
    Distance = [INF]*(n+1)
    Distance[start] = 0
    Sum = 0
    while Queue:
        dist, place = heapq.heappop(Queue)
        
        if  Distance[place] < dist:
            continue        

        Distance[place] = dist

        for value in Information[place]:    
            if  dist+value[1] < Distance[value[0]]: 
                Distance[value[0]] = dist+value[1]
                heapq.heappush(Queue, (dist+value[1], value[0]))
    
    for i in range(1, n+1):
        if Distance[i] <= m: Sum += Items[i]
    return Sum

Answer = 0
for j in range(1, n+1):
    S = solution(j)
    if S > Answer: Answer = S
print(Answer)