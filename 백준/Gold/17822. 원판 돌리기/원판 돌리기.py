n, m, t = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(n)]
rotate = [tuple(map(int, input().split())) for _ in range(t)]
ridx = [m] * n
getcidx = lambda i, j: (ridx[i] + j) % m
for x, d, k in rotate:
    for i in range(x, n+1, x):
        ridx[i-1] = (ridx[i-1] + k * (-1 if d == 0 else 1)) % m
    total = sum(map(sum, circle))
    willerase = []
    if total == 0: continue
    for i in range(n):
        for j in range(m):
            l, r = getcidx(i, j), getcidx(i, j+1)
            if circle[i][l] == circle[i][r] and circle[i][l] != 0:
                willerase.extend([(i, l), (i, r)])
    for i in range(n - 1):
        for j in range(m):
            l , r = getcidx(i, j), getcidx(i+1, j)
            if circle[i][l] == circle[i+1][r] and circle[i][l] != 0:
                willerase.extend([(i, l), (i+1, r)])
    if willerase:
        for i, j in willerase:
            circle[i][j] = 0
    else:
        avg = total / (n * m - sum(map(lambda x: x.count(0), circle)))
        for i in range(n):
            for j in range(m):
                if circle[i][j] == 0: continue
                if circle[i][j] < avg:
                    circle[i][j] += 1
                elif circle[i][j] > avg:
                    circle[i][j] -= 1
print(sum(map(sum, circle)))
        