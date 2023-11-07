import sys

N = int(input())
List = []

for i in range(N):
   Word = sys.stdin.readline().rstrip()
   if [Word, len(Word)] not in List:
    List.append([Word, len(Word)])

List.sort(key = lambda x: (x[1], x[0]))

for j in List:
   print(j[0])