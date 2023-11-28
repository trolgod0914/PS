from bisect import *
import sys; input = sys.stdin.readline

while True:
    try:
        N = int(input())
        if N == 0:
            print(0)
        else:
            Sequence = list(map(int, input().split()))
            INF = int(1e9)
            Array = [-INF]
            List = [(-INF, 0)]
            for i in range(0, N):
                if Sequence[i] > Array[-1]:
                    Array.append(Sequence[i])
                    List.append((Sequence[i], len(Array)-1))
                else:
                    idx = bisect_left(Array, Sequence[i])
                    Array[idx] = Sequence[i]
                    List.append((Sequence[i], idx))

            key = len(Array)-1
            print(key)
    except:
        break