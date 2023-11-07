import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def DPQ(N):
    Max_Queue = []
    Min_Queue = []
    Dict = defaultdict(int)
    for j in range(N):
        Order, Value = map(str, input().split())
        Value = int(Value)
        if Order == 'I':
            Dict[Value] += 1
            heapq.heappush(Max_Queue, -Value)
            heapq.heappush(Min_Queue, Value)
        else:
                if Value == 1:
                    while Max_Queue:
                        A = heapq.heappop(Max_Queue)
                        if Dict[-A] != 0:
                            Dict[-A] -= 1
                            break
                else:
                    while Min_Queue:
                        A = heapq.heappop(Min_Queue)
                        if Dict[A] != 0:
                            Dict[A] -= 1
                            break

    while Max_Queue and Dict[-Max_Queue[0]] == 0:
        heapq.heappop(Max_Queue)
    
    while Min_Queue and Dict[Min_Queue[0]] == 0:
        heapq.heappop(Min_Queue)

    if not Min_Queue:
        print('EMPTY')
    else:
        print(-Max_Queue[0], Min_Queue[0])

for x in range(int(input())):
    DPQ(int(input()))