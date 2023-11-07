import sys
input = sys.stdin.readline

Array = []
Answer = []

while True:
    A = input().rstrip()

    if A == ".":
        break

    num_1 = 0
    num_2 = 0
    check_1 = [-1]
    check_2 = [-1]

    for i in range(len(A)):
        if A[i] == '(':
            num_1 += 1
            check_1.append(i)
        if A[i] == ')':
            if check_1[-1] < check_2[-1]: 
                break
            check_1.pop()
            num_1 -= 1
        if A[i] == '[':
            num_2 += 1
            check_2.append(i)
        if A[i] == ']':
            if check_1[-1] > check_2[-1]:
                break
            check_2.pop()
            num_2 -= 1

        if num_1 < 0 or num_2 < 0: break
    
    if num_1 == 0 and num_2 == 0:
        print('yes')
    else:
        print('no')