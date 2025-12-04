import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cmd = [tuple(map(int, input().split())) for _ in range(m)]
cmd = [(d-1, s) for d, s in cmd]
dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
idx = lambda x: x % n
clouds = set([(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)])
for d, s in cmd:
    di, dj = dirs[d]
    di, dj = di * s, dj * s
    clouds = set([ (idx(i + di), idx(j + dj)) for i, j in clouds ])
    for i, j in clouds:
        a[i][j] += 1
    adds = [0] * len(clouds)
    for cidx, (i, j) in enumerate(clouds):
        for didx in range(1, len(dirs), 2):
            di, dj = dirs[didx]
            ai, aj = i + di, j + dj
            if not (0 <= ai < n and 0 <= aj < n): continue
            if a[ai][aj] > 0: adds[cidx] += 1
    for cidx, (i, j) in enumerate(clouds):
        a[i][j] += adds[cidx]
    nclouds = set()
    for i in range(n):
        for j in range(n):
            if a[i][j] > 1 and (i, j) not in clouds:
                nclouds.add((i, j))
                a[i][j] -= 2
    clouds = nclouds
result = 0
for row in a:
    for water in row:
        result += water
print(result)