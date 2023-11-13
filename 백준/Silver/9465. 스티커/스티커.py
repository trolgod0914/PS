import sys
sys.setrecursionlimit(1000000)
def Score(memo, N):
    if N > 2 and len(memo) < N:
        A, B, C, D, E = Score(memo, N-1)
        memo.append((max(B, E) + Array[0][N-1], max(A, D) + Array[1][N-1], max(A, B, C, D, E), C + Array[0][N-1], C + Array[1][N-1]))
    return memo[N-1]

for _ in range(int(input())):
    N = int(input())
    Array = [list(map(int, input().split())) for _ in range(2)]
    if N == 1:
        memo = [(0, Array[0][0], Array[1][0], 0, 0)]
    else:
        memo = [(Array[0][0], Array[1],[0], 0, Array[0][0], Array[1],[0]),
                (Array[1][0] + Array[0][1], Array[0][0] + Array[1][1], max(Array[0][0], Array[1][0]), Array[0][1], Array[1][1])]
    print(max(Score(memo, N)))