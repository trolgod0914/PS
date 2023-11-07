import sys
input = sys.stdin.readline
Array = list(input().strip().split('-'))
List = []
for i in Array:
    Value = list(map(int, i.split('+')))
    List.append(sum(Value))

Sum = List[0]
print(Sum * 2 - sum(List))