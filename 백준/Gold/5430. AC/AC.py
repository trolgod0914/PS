import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
for i in range(int(input().rstrip())):
    Order = list(input().rstrip())
    N = int(input().rstrip())
    array = deque(input()[1:-2].split(','))
    if array == deque(['']):
        array = deque([])
    value = 1
    key = True
    for j in Order:
        if j == 'R':
            value *= -1
        else:
            if len(array) > 0:
                if value > 0:
                    array.popleft()
                else:
                    array.pop()
            else:
                key = False
                break
    if value < 0:
        array.reverse()
    if key:
        print('['+','.join(array)+']'+'\n')
    else:
        print('error'+'\n')