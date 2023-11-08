from collections import deque
N = int(input())
array = list(map(int, input().split()))
answer = []
Dict = {}
for i in array:
    if i not in Dict:
        Dict[i] = 1
key = list(Dict.keys())
key.sort()
key = deque(key)
num = 0
while key:
    Dict[key.popleft()] = num
    num += 1
for j in array:
    answer.append(Dict[j])
print(*answer)