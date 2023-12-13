from collections import defaultdict
Weight = defaultdict(int)
Array = [0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
List = []
for _ in range(int(input())):
    List.append(input())
for Word in List:
    K = len(Word)
    for i in range(K):
        Weight[Word[i]] += Array[K-i]
Key = list(Weight.values())
Key.sort(reverse=True)
num = 9
Answer = 0
for k in Key:
    Answer += k*num
    num -= 1
print(Answer)