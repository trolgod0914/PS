import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
List = list(map(int, input().split()))
Deque = deque([])
    
for i in range(N):
    while Deque:
        key = Deque[-1]
        if key[1] <= List[i]:
            break
        else:
            Deque.pop()
    Deque.append((i, List[i]))
    if Deque[0][0] <= i-L:
        Deque.popleft()
    Answer = Deque[0][1]
    print(Answer, end=' ')