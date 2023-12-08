Array = list(input())
K = len(Array)
Value = {Array[i]: i+1 for i in range(K)}
Text = list(input())
M = len(Text)
Mod = 900528
Answer = 0
Key = 1
for j in range(1, M+1):
    Answer = (Answer + Value[Text[M-j]] * Key) % Mod
    Key = (Key * K) % Mod
print(Answer)