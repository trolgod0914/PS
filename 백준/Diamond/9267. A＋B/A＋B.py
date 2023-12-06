import sys; input = sys.stdin.readline
import math

a, b, s = map(int, input().split())

def solution(a, b, s):
    # Exception_Case 1
    if a == 0 and b == 0:
        if s == 0:
            print('YES')
        else:
            print('NO')
        exit()

    # Exception_Case 2
    if a == 0:
        if s % b == 0:
            print('YES')
        else:
            print('NO')
        exit()

    # Exception_Case 3
    if b == 0:
        if s % a == 0:
            print('YES')
        else:
            print('NO')
        exit()

    # Exception_Case 4
    if a == s or b == s:
        print('YES')
        exit()

    c = math.gcd(a, b)
    if c != 1:
        if s % c == 0:
            solution(a//c, b//c, s//c)
        else:
            print('NO')
            exit()

    x0, x1, y0, y1, r0, r1 = 1, 0, 0, 1, a, b

    while r0 % r1: # 유클리드 호제법
        q = r0 // r1
        x0, x1, y0, y1, r0, r1 = x1, x0, y1, y0, r1, r0
        x1 -= q * x0
        y1 -= q * y0
        r1 %= r0

    x, y = x1*s, y1*s # a*x + b*y = s로 만들어준다
    if x <= 0 or x >= b: # 조건에 맞는 X값 후보 하나를 선택한다
        z = x // b
        x %= b
        y += z * a

    while True:

        if x > 0 and y > 0:
            if math.gcd(x, y) == 1:
                if a*x + b*y == s:
                    print('YES')
                    exit()

        if y <= 0: # x, y 중 하나라도 0보다 작거나 같으면 조건에 부합하지 않는다
            print('NO')
            exit()

        # 적절한 값이 나올 때까지 반복한다.
        x += b
        y -= a

solution(a, b, s)