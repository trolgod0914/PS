import math
A = int(input())
A //= 2
if A == 0: print(1); exit()
Answer = 1
d = 1
for i in range(1, A):
    Answer *= A+1+i
    d *= i
    gcd = math.gcd(Answer, d)
    Answer, d = Answer//gcd, d//gcd

Answer //= A
print(Answer%987654321)