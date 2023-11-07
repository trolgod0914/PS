import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def trans_1000(a, b, c, d):
    return ((a*10+b)*10+c)*10+d

def trans_1(x):
    a, b, c, d = x//1000, (x%1000)//100, (x%100)//10, x%10
    return a, b, c, d

def BFS(A, B, array):
    Queue = deque([(A, '')])
    array[A] = True
    while Queue:
        x, answer = Queue.popleft()
        a, b, c, d = trans_1(x)
        if x == B:
            return answer+'\n'
        for i in 'DSLR':
            if i == 'D':
                num = (x*2)%10000
            if i == 'S':
                num = (x-1)%10000
            if i == 'L':
                num = trans_1000(b, c, d, a)
            if i == 'R':
                num = trans_1000(d, a, b, c)
            if not array[num]:
                Queue.append((num, answer+i))
                array[num] = True

for j in range(int(input())):
    array = [False for k in range(10000)]
    A, B = map(int, input().split())
    print(BFS(A, B, array))