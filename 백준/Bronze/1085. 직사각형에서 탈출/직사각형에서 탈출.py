x, y, w, h = map(int, input().split())
array = [x, y, w-x, h-y]
print(min(array))