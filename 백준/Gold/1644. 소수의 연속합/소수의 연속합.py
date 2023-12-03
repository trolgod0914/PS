import math

N = int(input())
if N == 1:
    print(0)
    exit()
List = [True for i in range(N+1)]
Array = []

for i in range(2, int(math.sqrt(N))+1):
    if List[i] == True:
        j = 2 
        while i * j <= N:
            List[i * j] = False
            j += 1

for k in range(2, N+1):
    if List[k]:
        Array.append(k)

M = len(Array)
end, Sum, Answer = 0, 0, 0

for start in range(M):
    while Sum < N and end < M:
        Sum += Array[end]
        end += 1
    if Sum == N:
        Answer += 1
    Sum -= Array[start]

print(Answer) 