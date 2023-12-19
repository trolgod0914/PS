import sys; input = sys.stdin.readline
x, y, c = map(float, input().split())
z = min(x, y)
start = 0
end = z
while start <= end:
    mid = (start+end)/2
    A, B = (x**2-mid**2)**(0.5), (y**2-mid**2)**(0.5)
    C = round(A*B/(A+B), 6)
    if C == c:
        break
    if C > c:
        start = mid
    if C < c:
        end = mid
print(mid)