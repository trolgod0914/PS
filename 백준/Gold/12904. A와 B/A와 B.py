S = list(input())
T = list(input())
s = len(S)
while len(T) > s:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
if ''.join(S) == ''.join(T):
    print(1)
else:
    print(0)