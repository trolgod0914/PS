import sys; input = sys.stdin.readline
N = int(input())
K = int(input())
Array = list(map(int, input().split()))
Array.sort()
List = []
for i in range(N-1):
    List.append(Array[i+1]-Array[i])
List.sort()
if K-1 >= len(List):
    print(0)
else:
    for _ in range(K-1):
        List.pop()
    print(sum(List))