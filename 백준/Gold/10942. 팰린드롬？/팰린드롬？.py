import sys; input = sys.stdin.readline; print = sys.stdout.write

N = int(input())
Array = list(map(int, input().split()))
Answer = [['0\n']*N for _ in range(N)]
for i in range(N):
    for j in range(N-i):
        k = i+j
        if i == 0: Answer[j][k] = '1\n'
        elif i == 1:
            if Array[j] == Array[k]: Answer[j][k] = '1\n'
        else:
            if Array[j] == Array[k]:
                if Answer[j+1][k-1] == '1\n': Answer[j][k] = '1\n'
for _ in range(int(input())):
    S, E = map(int, input().split())
    print(Answer[S-1][E-1])