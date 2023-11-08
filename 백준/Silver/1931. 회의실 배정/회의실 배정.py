import sys
input = sys.stdin.readline
N = int(input())
array = []
for i in range(N):
    A, B = map(int, input().split())
    array.append([A, B])
array.sort(key=lambda x:x[0])
array.sort(key=lambda x:x[1])

key = 0
value = 0
count = 0

for j in array:
    if j[0] >= value:
        key, value = j[0], j[1]
        count +=1
print(count)