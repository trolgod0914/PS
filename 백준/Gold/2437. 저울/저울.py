import sys; input = sys.stdin.readline
N = int(input())
Weight = list(map(int, input().split()))
Weight.sort()
Answer = 1
for i in Weight:
    if Answer < i: break
    Answer += i
print(Answer)