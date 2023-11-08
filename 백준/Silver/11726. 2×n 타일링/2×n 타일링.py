memo = [1, 2]
def Tile(N):
    global memo
    if N > 2 and len(memo) < N:
        memo.append(Tile(N-2) + Tile(N-1))
    return memo[N-1]
print(Tile(int(input()))%10007)