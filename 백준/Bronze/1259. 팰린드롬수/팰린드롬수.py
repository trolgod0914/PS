Problem = []
Answer = []

while True:
    A = int(input())
    if A == 0:
        break
    else:
        Problem.append(A)

for i in Problem:
    i = str(i)
    if i == i[::-1]:
        Answer.append('yes')
    else:
        Answer.append('no')

for k in Answer:
    print(k)