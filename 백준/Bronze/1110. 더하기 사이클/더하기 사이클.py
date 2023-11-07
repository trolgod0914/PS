N = int(input())
count = 0
num_2 = N

while True:
    count += 1
    num_1 = num_2 // 10 + num_2 % 10
    num_2 = (num_2 % 10) * 10 + num_1 % 10
    if num_2 == N:
        break

print(count)