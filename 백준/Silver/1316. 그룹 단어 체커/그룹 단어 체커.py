Count = 0
for i in range(int(input())):
    text = input()
    Dict = {}
    key = True
    for j in text:
        if j not in Dict:
            Dict[j] = 1
            A = j
        else:
            if j == A:
                pass
            else:
                key = False
                break
    if key == True:
        Count+=1
print(Count)