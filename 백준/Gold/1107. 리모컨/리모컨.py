N = int(input())
M = int(input())
if M == 0:
    print(min(abs(N-100), len(str(N))))
else:
    array = list(map(int, input().split()))
    waste = {}
    for i in array:
        waste[i] = 1
    Dict = {x: 1 for x in range(1000000)}

    for j in list(waste.keys()):
        for k in list(Dict.keys()):
            if str(j) in str(k):
                Dict.pop(k)

    List = list(Dict.keys())
    answer = abs(N-100)
    for l in List:
        if abs(l-N)+len(str(l)) < answer:
            answer = abs(l-N)+len(str(l))
    print(answer)