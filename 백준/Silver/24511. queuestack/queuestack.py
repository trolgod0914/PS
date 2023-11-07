import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
queue_stack = deque(input().split())
Sequence_B = deque(input().split())
M = int(input().rstrip())
Sequence_C = input().split()
Deque = deque([])
answer = []
for i in range(N):
    A = queue_stack.popleft()
    B = Sequence_B.popleft()
    if A == '0':
        Deque.append(B)
for j in Sequence_C:
    Deque.appendleft(j)
    C = Deque.pop()
    answer.append(C)
print(*answer)