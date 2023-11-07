N = int(input())
Array = [0] * (N + 1)
for i in range(1, N+1):
    if i == 1:
        Array[i] += 0
    elif i == 2:
        Array[i] += 1
    elif i == 3:
        Array[i] += 1
    else:
        if i % 3 == 0:
            if i % 2 == 0:
                Array[i] += min(Array[i//3], Array[i//2]) + 1
            else:
                Array[i] += min(Array[i//3], Array[i-1]) + 1
        else:
            if i % 2 == 0:
                Array[i] += min(Array[i//2], Array[i-1]) + 1
            else:
                Array[i] += Array[i-1] + 1
print(Array[N])