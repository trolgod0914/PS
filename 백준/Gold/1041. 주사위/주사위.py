N = int(input())
A, B, C, D, E, F = map(int, input().split())
if N == 1: print(A+B+C+D+E+F-max(A, B, C, D, E, F)); exit()
q, w, e = min(A, F), min(B, E), min(C, D)
Min, Max = min(q, w, e), max(q, w, e)
Two, Three = q+w+e-Max, q+w+e
print(5*(N-2)*(N-2)*Min + 4*(N-2)*Min + 8*(N-2)*Two + 4*Two + 4*Three)