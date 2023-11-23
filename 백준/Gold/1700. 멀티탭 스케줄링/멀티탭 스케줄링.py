from collections import deque
import heapq
N, K = map(int, input().split())
Use_List = list(map(int, input().split()))
Order = [deque([]) for _ in range(K+1)]
Use_Order = []
Plug = []
heapq.heapify(Plug)
Check = [0] * (K+1)
Answer = 0

if N >= K:
    print(0); exit()

for i in range(K):
    Order[Use_List[i]].append(i)

for j in Order:
    try:
        j.popleft()
        j.append(K)
    except:
        pass

for k in Use_List:
    Use_Order.append((-Order[k].popleft(), k))

for item in Use_Order:
    if Check[item[1]] == 1:
        if Plug[-1][1] == item[1]:
            Plug[-1] = item
        else:
            Plug[-2] = item
        Recycle = heapq.heappop(Plug)
        heapq.heappush(Plug, Recycle)
    else:
        if len(Plug) < N:
            heapq.heappush(Plug, item)
            Check[item[1]] = 1
        else:
            discard = heapq.heappop(Plug)
            Check[discard[1]] = 0
            heapq.heappush(Plug, item)
            Check[item[1]] = 1
            Answer += 1
print(Answer)