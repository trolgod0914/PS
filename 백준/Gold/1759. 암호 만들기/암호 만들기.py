from itertools import combinations
L, C = map(int, input().split())
Array = list(input().split())
Array.sort()
Vowel = []
for Alpah in Array:
    if Alpah in 'aeiou':
        Vowel.append(Alpah)

Consonant = list(set(Array)-set(Vowel))
Consonant.sort()
all = set(combinations(Array, L))
for C in Consonant:
    T = Vowel + [C]
    T.sort()
    all -= set(combinations(T, L))
all -= set(combinations(Consonant, L))
Answer = []
for i in all:
    Answer.append(''.join(i))
Answer.sort()
for j in Answer:
    print(j)