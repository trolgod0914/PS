import sys
input = sys.stdin.readline
print = sys.stdout.write

def star(N):
    # N == 1인 경우
    if N == 1:
        test_case = [['*']]
        return test_case
    
    # 구하고 싶은 test_case 생성
    M = N-1
    K = 2**(N+1)-3
    L = 2**N-1
    I = 2**M-1
    O = 2**(M+1)-3
    base_case = star(M)
    test_case = [[' ']*K for x in range(L)]

    if M % 2 == 1:
        test_case[0] = ['*']*K
        for i in range(1, L):
            test_case[i][i] = '*'
            test_case[i][K-i-1] = '*'
        for j in range(1, I+1):
            test_case[j][I+1:I+O+1] = base_case[j-1]

    else:
        test_case[-1] = ['*']*K
        for i in range(L):
            test_case[i][L-1-i] = '*'
            test_case[i][L-1+i] = '*'
        for j in range(I):
            test_case[j+I][I+1:I+O+1] = base_case[j]
    return test_case

N = int(input())
answer = star(N)
for k in answer:
    print(''.join(k).rstrip()+'\n')