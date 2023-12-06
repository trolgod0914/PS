from math import *
List = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
N = int(input())
M = int(input())
def Soccer(N):
    Answer = 0
    for time in List:
        Answer += comb(18, time) * (N**time) * ((100-N)**(18-time))
    return Answer

print(1-(Soccer(N)*Soccer(M)/(100**36)))