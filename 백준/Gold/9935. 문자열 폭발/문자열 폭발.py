from collections import deque
import itertools
Text = deque(list(input()))
Bomb = deque(list(input()))
key = len(Bomb)
Answer = deque([])
while len(Text) >= key:
    if deque(itertools.islice(Text, 0, key)) == Bomb:
        for _ in range(key):
            Text.popleft()
        for _ in range(key-1):
            if Answer:
                Text.appendleft(A:=Answer.pop())
    else:
        Answer.append(A:=Text.popleft())
Answer += Text
if Answer:
    print(''.join(Answer))
else:
    print('FRULA')