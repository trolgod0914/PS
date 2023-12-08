def Num_Playing(Array, N):
    if N == 2:
        A, B, C = Array[0], Array[1], Array[2]
        if not isinstance(A, int):
            a, b, c, K = sum(A), sum(B), sum(C), len(A)
            if not (a + b) % (K*2):
                return A + B
            elif not (a + c) % (K*2):
                return A + C
            else:
                return B + C
        else:
            a, b, c, K = A, B, C, 1
            if not (a + b) % (K*2):
                return [A] + [B]
            elif not (a + c) % (K*2):
                return [A] + [C]
            else:
                return [B] + [C]
    else:
        M = N//2
        List = []
        while len(Array) >= N-1:
            L1, L2 = Array[:N-1], Array[N-1:]
            L = Num_Playing(L1, M)
            List.append(L)
            for i in L:
                L1.remove(i)
            Array = L1 + L2
        return Num_Playing(List, 2)

N = int(input())
List = list(map(int, input().split()))
print(*Num_Playing(List, N))