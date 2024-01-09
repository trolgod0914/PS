import sys; input = sys.stdin.readline
from collections import deque
N = int(input())
Answer = deque([])
Array = list(map(int, input().split()))
Array = Array[::-1]
for i in range(N):
    if Array[i] == 1: Answer.appendleft(i+1)
    if Array[i] == 2: A = Answer.popleft(); Answer.appendleft(i+1); Answer.appendleft(A)
    if Array[i] == 3: Answer.append(i+1)

print(*Answer)