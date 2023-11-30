import sys; input = sys.stdin.readline
N = int(input())
Liquid = list(map(int, input().split()))
Chraracter = 2000000000
Start, End = 0, N-1
Min, Max = Liquid[0], Liquid[-1]

while Start < End:
    Sum = Liquid[Start] + Liquid[End]
    if abs(Sum) < Chraracter:
        Chraracter, Min, Max = abs(Sum), Liquid[Start], Liquid[End]
    if Sum < 0:
        Start += 1
    if Sum > 0:
        End -= 1
    if Sum == 0:
        break

print(Min, Max)