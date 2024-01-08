import sys; input = sys.stdin.readline
Array = list(map(int, input().split()))
DP = [[[int(1e6) for _ in range(5)] for _ in range(5)] for _ in range(len(Array))]
DP[0][0][0] = 0

def Move(current, next):
    if current == 0: return 2
    if current == next: return 1
    if (current+next)%2: return 3
    return 4

for i in range(1, len(Array)):
    V = Array[i-1]

    for l in range(5):
        for r in range(5):
            if r == V: continue
            DP[i][V][r] = min(DP[i][V][r], DP[i-1][l][r] + Move(l, V))

    for r in range(5):
        for l in range(5):
            if l == V: continue
            DP[i][l][V] = min(DP[i][l][V], DP[i-1][l][r] + Move(r, V))
    
Answer = int(1e9)
for l in range(5):
    Answer = min(Answer, min(DP[-1][l]))

print(Answer)