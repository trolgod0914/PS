import sys; sys.setrecursionlimit(1000000); input = sys.stdin.readline
PreOrder = []

while True:
    try:
        PreOrder.append(int(input()))
    except:
        break

def PostOrder_by_BinarySearch(Start, End):
    if Start > End:
        return
    Check = End + 1
    for idx in range(Start + 1, End + 1):
        if PreOrder[idx] > PreOrder[Start]:
            Check = idx
            break
    PostOrder_by_BinarySearch(Start + 1, Check-1)
    PostOrder_by_BinarySearch(Check, End)
    print(PreOrder[Start])

PostOrder_by_BinarySearch(0, len(PreOrder)-1)