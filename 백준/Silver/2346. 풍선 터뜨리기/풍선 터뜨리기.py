import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
Order = deque(input().split())
Deque = deque([])
answer = []

for i in range(N):
    A = Order.popleft()
    Deque.append([i+1, -int(A)])

key = 0
while Deque:
    Deque.rotate(key)
    O = Deque.popleft()
    result = O[0]
    key = O[1]
    if key < 0:
        key += 1
    answer.append(result)

print(*answer)