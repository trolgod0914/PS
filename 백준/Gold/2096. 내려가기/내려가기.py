import sys; input = sys.stdin.readline
for i in range(N:=int(input())):
    A, B, C = map(int, input().split())
    if N == 1:
        Min = min(A, B, C)
        Max = max(A, B, C)
        break
    else:
        if i == 0:
            left, right = min(A, B), min(B, C)
            Left, Right = max(A, B), max(B, C)
            mid, Mid = min(left, right), max(Left, Right)
            Record = [[left, Left], [mid, Mid], [right, Right]]
            continue
        
        a, b, c, d, e, f = Record[0][0] + A, Record[0][1] + A, Record[1][0] + B, Record[1][1] + B, Record[2][0] + C, Record[2][1] + C
        if i == N-1:
            Min = min(a, c, e)
            Max = max(b, d, f)
            break
        
        left, right = min(a, c), min(c, e)
        Left, Right = max(b, d), max(d, f)
        mid, Mid = min(left, right), max(Left, Right)
        Record = [[left, Left], [mid, Mid], [right, Right]]

print(Max, Min)