N = int(input())
Sequence = list(map(int, input().split()))
Max_Sum = [0]*N
Max_Sum[0] = Sequence[0]

for term in range(1, N):
    for term_check in range(term):
        if Sequence[term_check] < Sequence[term]:
            Max_Sum[term] = max(Max_Sum[term], Max_Sum[term_check] + Sequence[term])
        else:
            Max_Sum[term] = max(Max_Sum[term], Sequence[term])

print(max(Max_Sum))