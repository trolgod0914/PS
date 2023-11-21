import sys
input = sys.stdin.readline
print = sys.stdout.write

def star(N):
    # N == 0인 경우
    if N == 0:
        test_case = [['*']]
        return test_case
    if N == 1:
        test_case = [[' ', ' ', '*', ' ', ' '],
                     [' ', ' ', '*', ' ', ' '],
                     ['*', '*', '*', '*', '*'],
                     [' ', '*', '*', '*', ' '],
                     [' ', '*', ' ', '*', ' ']]
        return test_case
    # 구하고 싶은 test_case 생성
    M = N-1
    K = 5**(M)
    base_case = star(M)
    test_case = [[' ']*(5**N) for x in range(5**N)]
    for i in range(K):
        test_case[i][2*K:3*K] = base_case[i]
        test_case[i+K][2*K:3*K] = base_case[i]
        test_case[i+2*K] = base_case[i] * 5
        test_case[i+3*K][K:4*K] = base_case[i] * 3
        test_case[i+4*K][K:2*K] = base_case[i]
        test_case[i+4*K][3*K:4*K] = base_case[i]
    return test_case

N = int(input())
answer = star(N)
for k in answer:
    print(''.join(k)+'\n')