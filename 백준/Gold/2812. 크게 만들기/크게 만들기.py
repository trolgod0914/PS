import sys; input = sys.stdin.readline
N, K = map(int, input().split())
Number = list(input().rstrip())
Stack = []
Delete = []
for idx in range(N):
    while Stack and len(Delete) < K:
        if int(Stack[-1]) < int(Number[idx]):
            Delete.append(Stack.pop())
        else:
            break
    Stack.append(Number[idx])
L = len(Delete)
for _ in range(K-L):
    Stack.pop()
print(''.join(Stack))