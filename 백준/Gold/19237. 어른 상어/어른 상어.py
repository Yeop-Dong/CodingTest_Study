import sys
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
smell = [ [[0, 0] for _ in range(n)] for _ in range(n)]
shark = [None] * (m+1)
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            shark[grid[i][j]] = (i, j)
            smell[i][j] = [grid[i][j], k]
shdir = [None] + [d-1 for d in list(map(int, input().split()))] 
shdpr = [None] + [[[d-1 for d in list(map(int, input().split()))] for _ in range(4)] for _ in range(m)]
cnt = 0
while not all(sh is None for sh in shark[2:]) and cnt < 1001:
    cnt += 1
    nshark = [None] * (m + 1)
    for idx in range(1, m+1):
        if shark[idx] is None: continue
        i, j = shark[idx]
        pr = shdpr[idx][shdir[idx]]
        nd, mysmell = None, []
        for d in pr:
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if smell[ni][nj][0] == 0:
                    nd = d
                    break
                if smell[ni][nj][0] == idx:
                    mysmell.append(d)
        if nd is None and mysmell:
            nd = mysmell[0]
        if nd is None:
            nshark[idx] = shark[idx]
            continue
        di, dj = dirs[nd]
        ni, nj = i + di, j + dj
        nshark[idx] = (ni, nj)
        shdir[idx] = nd
    for i in range(n):
        for j in range(n):
            if smell[i][j][0] != 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0
    grid = [[0] * n for _ in range(n)]
    shark = nshark
    for idx in range(m, 0, -1):
        if shark[idx] is None:
            continue
        i, j = shark[idx]
        if grid[i][j] != 0:
            shark[grid[i][j]] = None
        grid[i][j] = idx
        smell[i][j] = [idx, k]
print(cnt if cnt != 1001 else -1)