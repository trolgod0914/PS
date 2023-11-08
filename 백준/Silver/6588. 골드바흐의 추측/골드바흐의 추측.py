import math
import sys
input = sys.stdin.readline
print = sys.stdout.write
Sieve = [True for x in range(1000001)]
Sieve[0] = False
Sieve[1] = False
Dict = {}

for i in range(1000, 1, -1):
    if Sieve[i] == True:
        Key = 2
        while i * Key <= 1000000:
            Sieve[i * Key] = False
            Key += 1

for j in range (3, 1000000, 2):
    if Sieve[j]:
        Dict[j] = 1

def goldbach(N):
    global Dict
    if N == 0:
        return False
    for i in range(3, N//2+1, 2):
        if i in Dict:
            if N-i in Dict:
                return [str(i), str(N-i)]
    return "Goldbach's conjecture is wrong."

while 1:
    n = int(input())
    A = goldbach(n)
    if A == False:
        break
    if type(A) == list:
        print(str(n))
        print(' = ')
        print(' + '.join(A) + '\n')
    else:
        print(str(A) + '\n')