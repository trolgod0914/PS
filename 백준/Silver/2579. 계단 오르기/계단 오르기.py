import sys
input = sys.stdin.readline
Score = {'1': 0,
         '2': 0,
         '3': 0,
         '4': 0}
N = int(input())
for i in range(N):
    Score[str(i+1)] = int(input())
memo = [(0, Score['1']),
        (Score['2'], Score['1']+Score['2'])]
def stair(N):
    global memo
    global Score
    A = Score[str(N)]
    if N > 2 and len(memo) < N:
        x, y = stair(N-2)
        a, b= stair(N-1)
        memo.append((max(x, y)+A, a+A))
    return memo[N-1]

print(max(stair(N)))