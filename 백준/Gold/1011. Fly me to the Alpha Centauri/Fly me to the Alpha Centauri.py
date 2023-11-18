import sys
input = sys.stdin.readline
print = sys.stdout.write

def Find_way(N, M):
    Place = (M-N+1)//2
    num = 1
    while Place >= num:
        Place -= num
        if Place > 0:
            num += 1
    if (M-N)-(num*(num-1)) <= num:
        return num*2-1
    else:
        return num*2
    
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(str(Find_way(x, y))+'\n')