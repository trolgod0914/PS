import math, sys; input = sys.stdin.readline
def solution():
    N = int(input())
    M = int(1e6)
    Array = list(map(int, input().split()))
    K = int(math.sqrt(M))
    Score = [0]*(M+1)
    Dict = {x: 1 for x in Array}
    for i in Array:
        j = 2
        while (k := i * j) <= M:
            if k in Dict:
                Score[k] -= 1
                Score[i] += 1
            j += 1
    for i in Array:
        print(Score[i], end=' ')

solution()