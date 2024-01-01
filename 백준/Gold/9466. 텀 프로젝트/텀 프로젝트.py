import sys; input = sys.stdin.readline

def DFS(num):
    List = []
    while visited[num]:
        visited[num] = False
        List.append(num)
        num = Array[num]
    if num in List:
        return len(List) - List.index(num)
    return 0

    
for _ in range(int(input())):
    N = int(input())
    Array = [0] + list(map(int, input().split()))
    visited = [True]*(N+1)
    Answer = N
    for i in range(1, N+1):
        if not visited[i]: continue
        Answer -= DFS(i)
    print(Answer)