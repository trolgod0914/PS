import sys, heapq; input = sys.stdin.readline
Left, Right = [], []
for i in range(int(input())):
    value = int(input())
    if i == 0:
        print(Answer := value)
    else:
        if len(Left) == len(Right):
            if Left and Right:
                Small = -heapq.heappop(Left)
                Large = heapq.heappop(Right)
                A = [Small, value, Answer, Large]
                A.sort()
                heapq.heappush(Left, -A[0])
                heapq.heappush(Right, A[2])
                heapq.heappush(Right, A[3])
                Answer = A[1]
            else:
                if value >= Answer:
                    heapq.heappush(Right, value)
                else:
                    heapq.heappush(Right, Answer)
                    Answer = value
        elif len(Left) > len(Right):
            if value >= Answer:
                heapq.heappush(Right, value)
            else:
                Small = -heapq.heappop(Left)
                heapq.heappush(Right, Answer)
                if Small <= value:
                    heapq.heappush(Left, -Small)
                    Answer = value
                else:
                    heapq.heappush(Left, -value)
                    Answer = Small
        else:
            if value <= Answer:
                heapq.heappush(Left, -value)
            else:
                Large = heapq.heappop(Right)
                heapq.heappush(Left, -Answer)
                if Large >= value:
                    heapq.heappush(Right, Large)
                    Answer = value
                else:
                    heapq.heappush(Right, value)
                    Answer = Large
        print(Answer)