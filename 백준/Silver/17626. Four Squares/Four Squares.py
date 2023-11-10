import math, sys
memo = {x:0 for x in range(1, 50001)}
N = int(input())
for i in range(1, 224):
    memo[i**2] = 1
    memo[2*(i**2)] = 2
    memo[3*(i**2)] = 3
def Four_Squares(N):
    if memo[N] == 0:
        array = []
        for i in range(int(math.sqrt(N/2)), int(math.sqrt(N))+1):
            array.append(Four_Squares(N-(i**2)) + 1)
        memo[N] = min(array)
    return memo[N]

print(Four_Squares(N))