import sys; input = sys.stdin.readline
N, S = map(int, input().split()) # 수열의 길이 N과 부분합 S를 입력받는다.
Array = list(map(int, input().split())) # 수열을 입력받는다.
Sum = 0 # 부분합
Answer = N+1 # 조건을 만족하는 수열의 최소 길이를 저장한다.
check = False # 조건을 만족하는 수열이 있는지 확인한다.
tail = 0 # Two Pointer을 위한 끝점 설정

for head in range(N):
    while Sum < S and tail < N:
        Sum += Array[tail]
        tail += 1
    
    if Sum >= S:
        check = True # 조건을 만족하는 수열이 있으므로 True
        if Answer > tail-head: # 수열의 길이와 min값을 비교한다.
            Answer = tail-head
    Sum -= Array[head]

if check:
    print(Answer)
else:
    print(0)