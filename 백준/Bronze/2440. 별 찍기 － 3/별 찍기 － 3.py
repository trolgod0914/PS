N = int(input())
Star = [['*']*(N-i) for i in range(N)]
for j in Star:
    print(''.join(j))