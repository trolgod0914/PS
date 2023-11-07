N = int(input())
Dict = {x: 0 for x in range(N)}
array = list(map(int, input().split()))
answer = 1
count = 0
value = 3
for i in array:
    if i not in Dict:
        answer = 0
        break
    Dict[i] += 1
    if Dict[i] > 2:
        answer = 0
        break
key = list(Dict.keys())
for j in key:
    if Dict[j] > value:
        answer = 0
        break
    count += Dict[j]
    if count == N and Dict[j] < 2:
        answer *= (Dict[j]+1)
        break
    answer *= Dict[j]
    value = Dict[j]
    if answer == 0:
        break
print(answer)