import sys; input = sys.stdin.readline

def solution():
    N = int(input())
    DP = [[0]*(N) for _ in range(N)]
    Array = [tuple(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        for start in range(N-i):
            end = start + i
            R1 = Array[start][0]
            R2, C2 = Array[end]
            if end-start == 1: DP[start][end] = R1*R2*C2
            else:
                R3 = Array[start+1][0]
                DP[start][end] = min(DP[start+1][end] + R1*R3*C2, DP[start][end-1] + R1*R2*C2)
                for idx in range(start+1, end-1):
                    R3 = Array[idx+1][0]
                    DP[start][end] = min(DP[start][end], DP[start][idx]+DP[idx+1][end]+R1*R3*C2)
    return print(DP[0][N-1])

solution()