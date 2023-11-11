from itertools import combinations
N, M = map(int, input().split())
answer = combinations(range(1, N+1), M)
for i in answer:
    print(*i)