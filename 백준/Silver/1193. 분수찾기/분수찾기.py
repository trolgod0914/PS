X = int(input())
num = 0
while 1:
    if num*(num+1)//2 < X <= (num+1)*(num+2)//2:
        key = X-(num*(num+1)//2)
        if num%2 == 1:
            N = key
            M = num+2-key
        else:
            N = num+2-key
            M = key
        break
    num+=1
print(str(N)+'/'+str(M))