import sys
input = sys.stdin.readline
print = sys.stdout.write

def star(N):
    # N == 3인 base_case 지정
    if N == 3:
        test_case = [[' ', ' ', '*', ' ', ' '],
                     [' ', '*', ' ', '*', ' '],
                     ['*', '*', '*', '*', '*']]
        return test_case
    
    # 구하고 싶은 test_case 생성
    M = N//2
    base_case = star(M)
    test_case = [[' ']*(2*N-1) for x in range(N)]
    for i in range(M):
        test_case[i][M:M+N-1] = base_case[i]
    for j in range(M, N):
        test_case[j] = base_case[j-M] + [' '] + base_case[j-M]
    return test_case

N = int(input())
answer = star(N)
for k in answer:
    print(''.join(k)+'\n')