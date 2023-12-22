def solution():
    Dict = {}
    Array = [tuple(map(int, input().split())) for _ in range(4)]
    for i in range(3):
        x1, y1 = Array[i]
        for j in range(i+1, 4):
            x2, y2 = Array[j]
            d = (x1-x2)**2+(y1-y2)**2
            if d not in Dict:
                Dict[d] = 1
            else:
                Dict[d] += 1
    Key = list(Dict.keys())
    if len(Key) != 2: return print(0)
    A, B = Key[0], Key[1]
    if Dict[A] != 4 and Dict[B] != 4: return print(0)
    if A == B*2 or B == A*2: return print(1)
    else: return print(0)

for _ in range(int(input())):
    solution()