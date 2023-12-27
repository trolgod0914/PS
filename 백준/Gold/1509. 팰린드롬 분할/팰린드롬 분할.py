import sys; input = sys.stdin.readline

def Palindrome(Text, T):
    Palindrome_DP = [[False]*T for _ in range(T)]
    for i in range(T):
        for j in range(T-i):
            k = i+j
            if i == 0: Palindrome_DP[j][k] = True
            elif i == 1:
                if Text[j] == Text[k]: Palindrome_DP[j][k] = True
            else:
                if Text[j] == Text[k]:
                    if Palindrome_DP[j+1][k-1]: Palindrome_DP[j][k] = True
    return Palindrome_DP

def Segment(Palindrome_DP, T):
    DP = [2501]*T
    DP[0] = 1
    for end in range(1, T):
        for start in range(end+1):
            if Palindrome_DP[start][end]:
                if not start: DP[end] = 1
                else: DP[end] = min(DP[end], DP[start-1]+1)
            else:
                DP[end] = min(DP[end], DP[end-1]+1)

    return print(DP[T-1])

def solution():
    Text = list(input().rstrip())
    T = len(Text)
    return Segment(Palindrome(Text, T), T)

solution()