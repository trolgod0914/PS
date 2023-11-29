import sys; input = sys.stdin.readline
INF = int(1e9)

def solution(N, Information):
    Standard = [INF] * (N+1)
    Standard[N] = 0
    for i in range(N):
        for Start, End, Weight in Information:
            if Standard[End] > Standard[Start] + Weight:
                Standard[End] = Standard[Start] + Weight
                if i == N-1:
                    return 'YES'
    return 'NO'

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    Information = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        Information.append((S, E, T))
        Information.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        Information.append((S, E, -T))
    print(solution(N, Information))