import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
Land = {}

for i in range(N):
    Line = list(map(int, input().split()))
    for j in Line:
        if j not in Land:
            Land[j] = 1
        else:
            Land[j] += 1

Keys = list(Land.keys())
Keys = list(sorted(Keys, reverse=True))
start = min(Keys)
end = max(Keys)
Array = []
Answer = []

while start <= end:
    count = 0

    for k in Keys:
        count += Land.get(k) * (end-k)
    if count <= B:
        Array.append(end)
    end -= 1

for l in Array:
    num = 0
    for m in Keys:
        if m > l:
            num += Land.get(m) * (m-l) * 2
        else:
            num += Land.get(m) * (l-m)
    Answer.append(num)

Num = min(Answer)
print(Num, Array[Answer.index(Num)])