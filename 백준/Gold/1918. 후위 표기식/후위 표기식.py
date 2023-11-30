Text = input()
Answer = ''
Sign = []

for Letter in Text:
    if Letter == '(':
        Sign.append(Letter)
    if Letter == ')':
        while Sign[-1] != '(':
            Answer += Sign.pop()
        Sign.pop()
    if Letter == '*' or Letter == '/':
        while Sign and (Sign[-1] == '*' or Sign[-1] == '/'):
            Answer += Sign.pop()
        Sign.append(Letter)
    if Letter == '+' or Letter == '-':
        while Sign and Sign[-1] != '(':
            Answer += Sign.pop()
        Sign.append(Letter)
    if Letter.isalpha():
        Answer += Letter

while Sign:
    Answer += Sign.pop()

print(Answer)