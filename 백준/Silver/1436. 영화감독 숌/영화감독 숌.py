N = int(input())
count = 1
A = 1665
if N == 1:
    print(666)
else:
    while count != N:
        A += 1
        for i in range(len(str(A))-2):
            if str(A)[i] == str(A)[i+1] == str(A)[i+2] == '6':
                count += 1
                break
    print(A)