N = int(input())
Array = list(map(int, input().split()))

if N == 1:
    print(-1)
    exit()

key = []
for i in range(N-1):
    if Array[i] < Array[i+1]:
        key.append(i)

if key:
    K = key[-1]
else:
    print(-1)
    exit()

value = Array[K]
for j in range(K+1, N):
    if Array[j] > value:
        idx = j

Array[K], Array[idx] = Array[idx], Array[K]
Left, Right = Array[:K+1], Array[K+1:]
Right.sort()
Answer = Left + Right
print(*Answer)