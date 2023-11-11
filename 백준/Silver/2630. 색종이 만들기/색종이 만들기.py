import sys, copy, math
input = sys.stdin.readline

N = int(input())
Array = []
for _ in range(N):
    Array += list(map(int, input().split()))
Array = [Array]
Answer_white = []
Answer_blue = []

def four_division(array):
    key = int(math.sqrt(len(array)))//2
    array = [array[i:i+key] for i in range(0, len(array), key)]
    array_1 = sum(array[0::2], [])
    array_2 = sum(array[1::2], [])
    a1, a2, a3, a4 = array_1[:len(array_1)//2], array_1[len(array_1)//2:], array_2[:len(array_2)//2], array_2[len(array_2)//2:]
    return a1, a2, a3, a4

while Array:
    List = []
    for A in Array:
        if sum(A) == len(A):
            Answer_blue.append(A)
        elif sum(A) == 0:
            Answer_white.append(A)
        else:
            A1, A2, A3, A4 = four_division(A)
            List += [A1, A2, A3, A4]
    Array = copy.deepcopy(List)

print(len(Answer_white))
print(len(Answer_blue))