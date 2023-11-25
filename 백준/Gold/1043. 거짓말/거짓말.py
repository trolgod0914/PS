N, M = map(int, input().split())
Set = set(x+1 for x in range(N))
True_List = list(map(int, input().split()))
num, True_List = True_List[0], set(True_List[1:])
Set -= True_List
Answer = []
for _ in range(M):
    List = list(map(int, input().split()))
    Party = set(List[1:])
    if len(Party-True_List) < len(Party):
        True_List = True_List | Party
    else:
        Answer.append(Party)

for _ in range(M):
    Array = []
    for j in Answer:
        if len(j-True_List) < len(j):
            True_List = True_List | j
        else:
            Array.append(j)
    Answer = Array

print(len(Answer))