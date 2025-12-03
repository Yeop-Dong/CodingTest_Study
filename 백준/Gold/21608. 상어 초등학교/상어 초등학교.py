import sys
input = lambda: sys.stdin.readline().rstrip()
adjs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n = int(input())
st = [list(map(int, input().split())) for _ in range(n * n)]
stpos = {}
grid = [[0] * n for _ in range(n)]
for row in st:
    favor = row[1:]
    br, bc, badj, bmty = None, None, -1, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0: continue
            acnt, mcnt = 0, 0
            for di, dj in adjs:
                ai, aj = i + di, j + dj
                if 0 <= ai < n and 0 <= aj < n:
                    if grid[ai][aj] in favor: acnt += 1
                    elif grid[ai][aj] == 0: mcnt += 1
            if acnt > badj or (acnt == badj and mcnt > bmty):
                br, bc, badj, bmty = i, j, acnt, mcnt
    grid[br][bc] = row[0]
    stpos[row[0]] = (br, bc)
total = 0
for row in st:
    r, c = stpos[row[0]]
    favor = row[1:]
    fcnt = 0
    for dr, dc in adjs:
        ar, ac = r + dr, c + dc
        if 0 <= ar < n and 0 <= ac < n and grid[ar][ac] in favor:
            fcnt += 1
    if fcnt == 0: continue
    total += 10 ** (fcnt - 1)
print(total)
        
