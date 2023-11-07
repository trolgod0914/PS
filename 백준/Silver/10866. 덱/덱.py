import sys
from collections import deque

N = int(input())
Deque = deque()

for i in range(N):
    Order = sys.stdin.readline().rstrip()
    if 'push_front' in Order:
        Deque.appendleft(Order.split()[1])
    elif 'push_back' in Order:
        Deque.append(Order.split()[1])
    elif Order == 'pop_front':
        if len(Deque) == 0:
            print('-1')
        else:
            Front = Deque[0]
            Deque.popleft()
            print(Front)
    elif Order == 'pop_back':
        if len(Deque) == 0:
            print('-1')
        else:
            Back = Deque[-1]
            Deque.pop()
            print(Back)
    elif Order == 'size':
        print(len(Deque))
    elif Order == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif Order == 'front':
        if len(Deque) == 0:
            print('-1')
        else:
            front = Deque[0]
            print(front)
    elif Order == 'back':
        if len(Deque) == 0:
            print('-1')
        else:
            back = Deque[-1]
            print(back)