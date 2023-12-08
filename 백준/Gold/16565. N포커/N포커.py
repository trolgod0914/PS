from math import *
N = int(input())
Mod = 10007
if N <= 3: print(0); exit()
if N >= 40: print(comb(52, N)%Mod); exit()

T = N//4
Answer = 0
for i in range(1, T+1):
    Answer = (Answer + (comb(13, i) * comb(52-(4*i), N-(4*i)) * ((-1)**(i+1))))%Mod

print(Answer)