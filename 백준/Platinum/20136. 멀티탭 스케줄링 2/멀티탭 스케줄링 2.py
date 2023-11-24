import heapq
N, K = map(int, input().split())
if N >= K: print(0); exit() # N>=K면 뽑을 필요 X
Use_List = list(map(int, input().split()))
Order, Plug = [[] for _ in range(K+1)], []
Check, Use_Order = [0] * (K+1), [0] * (K+1) # Plug에 꽂혀있는지 확인 / 같은 전자기기를 몇 번 썼는지 기록
Answer, Count = 0, 0

for i in range(K):
    Order[Use_List[i]].append(i)

for item in Use_List:
    if Count == N and Check[item] == 0: # 꽂을 자리가 없는데, Plug에 꽂힌 것과 다를 때
        Discard = heapq.heappop(Plug)
        Check[Discard[1]] = 0 # 뺀 전자기기는 Check 0으로
        Answer += 1
        Count -= 1
    
    next_item_index = 0
    if Use_Order[item] == len(Order[item]) - 1: # 해당 전자기기를 마지막으로 사용할 때
        next_item_index = K
    else:
        Use_Order[item] += 1
        next_item_index = Order[item][Use_Order[item]]

    if Check[item] == 0:
        Check[item] = 1 # 꽂은 전자기기는 Check 1로
        Count += 1

    heapq.heappush(Plug, (-next_item_index, item))
    
print(Answer)