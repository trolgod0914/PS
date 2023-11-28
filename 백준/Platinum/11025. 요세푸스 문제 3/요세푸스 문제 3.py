N, K = map(int, input().split())
answer = 0
for i in range(1, N+1):
    answer = (answer+K)%i
print(answer+1)