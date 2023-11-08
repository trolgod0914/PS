import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Array = [int(input().rstrip()) for i in range(N)]
Array.sort(reverse=True)
answer = 0
for j in Array:
    answer += K//j
    K %= j
print(answer)