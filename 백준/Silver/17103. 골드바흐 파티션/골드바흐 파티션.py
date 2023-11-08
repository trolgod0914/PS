import math
import sys
input = sys.stdin.readline
print = sys.stdout.write
Sieve = {x: True for x in range(1000001)}
Sieve.pop(0)
Sieve.pop(1)

for i in range(1000, 1, -1):
    if Sieve[i] == True:
        Key = 2
        while i * Key <= 1000000:
            Sieve.pop(i * Key, None)
            Key += 1

for j in range(int(input())):
    N = int(input())
    count = 0
    for k in range(1, N//2+1):
        if k in Sieve and N-k in Sieve:
            count += 1
    print(str(count) + '\n')