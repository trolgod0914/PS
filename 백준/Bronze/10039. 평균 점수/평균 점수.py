Answer = 0
for _ in range(5):
    A = int(input())
    if A < 40: A = 40
    Answer += A
print(Answer//5)