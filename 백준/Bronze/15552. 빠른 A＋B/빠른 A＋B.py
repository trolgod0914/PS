import sys
T = int(input())
number_list = []
for i in range(0, T):
    a, b = sys.stdin.readline().rsplit()
    a = int(a)
    b = int(b)
    print(a + b)