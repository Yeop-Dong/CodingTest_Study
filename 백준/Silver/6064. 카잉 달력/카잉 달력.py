import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    if y == n: y = 0
    for i in range(n):
        year = i * m + x
        if year % n == y:
            print(year)
            break
    else:
        print(-1)
        