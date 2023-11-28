N = int(input())
Sequence = list(map(int, input().split()))
Max_Sum = [1]*N
Max_Sum[0] = 1

for term in range(1, N):
    for term_check in range(term):
        if Sequence[term_check] < Sequence[term]:
            Max_Sum[term] = max(Max_Sum[term], Max_Sum[term_check] + 1)
        else:
            Max_Sum[term] = max(Max_Sum[term], 1)

for term in range(1, N):
    for term_check in range(term):
        if Sequence[term_check] > Sequence[term]:
            Max_Sum[term] = max(Max_Sum[term], Max_Sum[term_check] + 1)
        else:
            Max_Sum[term] = max(Max_Sum[term], 1)

print(max(Max_Sum))