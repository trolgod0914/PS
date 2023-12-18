import sys; input = sys.stdin.readline; print = sys.stdout.write
for i in range(n:=int(input())):
    A, B, C = map(int, input().split())
    a, b, c = A**2, B**2, C**2
    print('Scenario #{}:\n'.format(str(i+1)))
    print('yes\n' if a+b+c == 2*max(a, b, c) else 'no\n')
    if i == n-1: break
    print('\n')