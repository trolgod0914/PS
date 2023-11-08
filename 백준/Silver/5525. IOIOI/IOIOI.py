import sys
input = sys.stdin.readline
N = int(input().strip())
M = int(input().strip())
S = input().strip().strip('O').replace('II', 'I I').replace('II', 'I I').replace('OO', 'O O').replace('OO', 'O O')
array = list(S.split('O'))
List = list(''.join(array).split())
count = 0
for i in List:
    if len(i) >= N+1:
        count += len(i)-N
print(count)