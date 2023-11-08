import heapq
import sys
print = sys.stdout.write
input = sys.stdin.readline
Array = []
heapq.heapify(Array)

for i in range(int(input())):
    x = int(input().rstrip())
    if x == 0:
        try:
            print(str(int(heapq.heappop(Array)) * (-1)) + '\n')
        except:
            print('0' + '\n')
    else:
        heapq.heappush(Array, x * (-1))