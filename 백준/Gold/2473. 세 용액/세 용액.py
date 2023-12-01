import sys; input = sys.stdin.readline
N = int(input())
Liquid = list(map(int, input().split()))
Liquid.sort()
Chraracter = 3000000000

for i in range(N-2):
    Start = i+1
    End = N-1
    while Start < End:
        Sum = Liquid[Start] + Liquid[End] + Liquid[i]
        if abs(Sum) < Chraracter:
            Chraracter, a, b, c = abs(Sum), Liquid[i], Liquid[Start], Liquid[End]
        if Sum < 0:
            Start += 1
        if Sum > 0:
            End -= 1
        if Sum == 0:
            break

print(a, b, c)