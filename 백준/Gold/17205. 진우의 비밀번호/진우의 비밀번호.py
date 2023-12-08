Value = [0, 1, 27, 703, 18279, 475255, 12356631, 321272407, 8353082583, 217180147159, 5646683826135]

N = int(input())
Text = list(input())
Answer = 0

for i in range(len(Text)):
    Answer += (ord(Text[i])-97) * Value[N-i] + 1
print(Answer)