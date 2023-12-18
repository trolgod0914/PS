import sys, math; input = sys.stdin.readline; print = sys.stdout.write
num = 0
while True:
    num += 1
    A, B, C = map(int, input().split())
    if not A: exit()
    if num > 1:
        print('\n')
    if A == -1:
        if B < C:
            Answer = 'a = {:.3f}\n'.format(math.sqrt(C**2-B**2))
        else:
            Answer = 'Impossible.\n'
    if B == -1:
        if A < C:
            Answer = 'b = {:.3f}\n'.format(math.sqrt(C**2-A**2))
        else:
            Answer = 'Impossible.\n'
    if C == -1:
        Answer = 'c = {:.3f}\n'.format(math.sqrt(A**2+B**2))
    print('Triangle #{}\n'.format(num))
    print(Answer)