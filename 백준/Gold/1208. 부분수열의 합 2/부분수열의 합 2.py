from itertools import combinations
from bisect import *
N, S = map(int, input().split())
Sequence = list(map(int, input().split()))
Answer = 0
# 수열을 분할
Sequence_Left = Sequence[0:N//2]
Sequence_Right = Sequence[N//2:]
# 분할한 수열의 부분수열 합 구하기
Left_Sum = []
Right_Sum = []

def Sum_of_Subsequence(seq, subseq_sum_list):
    for i in range(1, len(seq)+1):
        List = list(combinations(seq, i))
        for j in List:
            subseq_sum_list.append(sum(j))

Sum_of_Subsequence(Sequence_Left, Left_Sum)
Sum_of_Subsequence(Sequence_Right, Right_Sum)
Left_Sum.append(0)
Right_Sum.append(0)
Left_Sum.sort()
Right_Sum.sort()

for A in Left_Sum:
    Answer += bisect_right(Right_Sum, S-A)-bisect_left(Right_Sum, S-A)

print(Answer if S else Answer-1)