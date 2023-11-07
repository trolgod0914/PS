import sys

Store_0 = [1, 0]
Store_1 = [0, 1]
T = int(input())
Case = [sys.stdin.readline().strip() for i in range(T)]
Case_int = list(map(int, Case))

def fibonacci_times_0(Num_0):
    global Store_0
    if Num_0 >= 2 and len(Store_0) <= Num_0:
        Store_0.append(fibonacci_times_0(Num_0-1) + fibonacci_times_0(Num_0-2))
    return Store_0[Num_0]

def fibonacci_times_1(Num_1):
    global Store_1
    if Num_1 >= 2 and len(Store_1) <= Num_1:
        Store_1.append(fibonacci_times_1(Num_1-1) + fibonacci_times_1(Num_1-2))
    return Store_1[Num_1]

for j in Case_int:
    fibonacci_times_0(j)
    fibonacci_times_1(j)
    print(Store_0[j], Store_1[j])