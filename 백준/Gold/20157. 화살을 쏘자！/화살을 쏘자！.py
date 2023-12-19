import sys; input = sys.stdin.readline
from collections import defaultdict
N = int(input())
Dict = defaultdict(int)
Key = 0
for _ in range(N):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        Key += 1
    elif x == 0:
        if y > 0:
            Dict[0, 1] += 1
        else:
            Dict[0, -1] += 1
    elif y == 0:
        if x > 0:
            Dict[1, 0] += 1
        else:
            Dict[-1, 0] == 1
    elif x > 0:
        if y > 0:
            Dict[1, 1, y/x] += 1
        else:
            Dict[1, -1, y/x] += 1
    else:
        if y > 0:
            Dict[-1, 1, y/x] += 1
        else:
            Dict[-1, -1, y/x] += 1
print(max(list(Dict.values())) + Key)