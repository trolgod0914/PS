Dict = {'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F' : 0.0}
Score = 0
Subject = 0
for i in range(20):
    A, B, C = map(str, input().split())
    if C == 'P':
        pass
    else:
        Score += float(B)*Dict.get(C)
        Subject += float(B)
print(round(Score/Subject, 6))