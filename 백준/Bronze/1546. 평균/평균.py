Subject = int(input())
Score = [int(S) for S in input().split()]
Max = max(Score)
Average = 0
for i in range(len(Score)):
    Score[i-1] = (Score[i-1] / Max) * 100
for j in Score:
    Average += j
print(Average/Subject)