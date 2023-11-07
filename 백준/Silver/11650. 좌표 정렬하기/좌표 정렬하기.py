import sys
input = sys.stdin.readline

N = int(input())
Answer = []

for i in range(N):
    X, Y = map(int, input().split())
    Answer.append((X, Y))

Answer.sort(key=lambda x: (x[0],  x[1]))

for j in Answer:
    print(j[0], j[1])