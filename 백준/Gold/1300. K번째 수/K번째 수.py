def Count_idx(M, N):
    idx = 0
    for i in range(1, N+1):
        idx += min(M//i, N)
    return idx

def Binary_Search(N, K):
    start = 1
    end = K
    while start <= end:
        mid = (start+end)//2
        if Count_idx(mid, N) >= K:
            end = mid-1
        else:
            start = mid+1
    return start

N = int(input())
K = int(input())
print(Binary_Search(N, K))