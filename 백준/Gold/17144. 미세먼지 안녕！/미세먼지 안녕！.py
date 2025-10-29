import sys
input = lambda: sys.stdin.readline().rstrip()
r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
ap = None
for i in range(2, r):
    if a[i][0] == -1:
        ap = i
        break
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(t):
    na = [[0] * c for _ in range(r) ]
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                left = a[i][j]
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    spread = a[i][j] // 5
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj] != -1:
                        na[ni][nj] += spread
                        left -= spread
                na[i][j] += left
    a = na
    a[ap][0] = a[ap+1][0] = -1
    i, j = ap - 1, 0
    while i > 0: 
        a[i][j] = a[i-1][j]
        i -= 1
    while j < c - 1:
        a[i][j] = a[i][j+1]
        j += 1
    while i < ap:
        a[i][j] = a[i+1][j]
        i += 1
    while j > 1:
        a[i][j] = a[i][j-1]
        j -= 1
    a[i][j] = 0
    i, j = ap + 2, 0
    while i < r - 1:
        a[i][j] = a[i+1][j]
        i += 1
    while j < c - 1:
        a[i][j] = a[i][j + 1]
        j += 1
    while i > ap + 1:
        a[i][j] = a[i-1][j]
        i -= 1
    while j > 1:
        a[i][j] = a[i][j-1]
        j -= 1
    a[i][j] = 0
print(sum(map(sum, a)) + 2)