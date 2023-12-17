import sys; input = sys.stdin.readline
G = int(input())
Gate = [n for n in range(G+1)]
P = int(input())
answer = 0
for _ in range(P):
    num = int(input())
    K = Gate[num]
    while K > 0:
        if Gate[K] == K:
            Gate[num] = K
            Gate[K] -= 1
            break
        else:
            K = Gate[K]
    if not K: break
    answer += 1
print(answer)