import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Array = [list(map(int, input().split())) for _ in range(N)]

def prefix_sum(a, b, arr):
    prefixSum = [[0]*(a+1) for _ in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

Prefix_sum = prefix_sum(N, N, Array)

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(Prefix_sum[x2][y2] - Prefix_sum[x1-1][y2] - Prefix_sum[x2][y1-1] + Prefix_sum[x1-1][y1-1])