import sys
input = lambda: sys.stdin.readline().rstrip()
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rotate = [(0, -1), (1, 0), (0, 1), (-1, 0)]
n, m = map(int, input().split())
sy = sx = n // 2
grid = [list(map(int, input().split())) for _ in range(n)]
cmd = [tuple(map(int, input().split())) for _ in range(m)]
cmd = [(d - 1, s) for d, s in cmd]
bidpos = [[-1] * n for _ in range(n)]
bids = []
y, x = sy, sx
diff, d = 1, 0
i = 0
while i < n * n - 1:
    dy, dx = rotate[d]
    for _ in range(diff):
        y, x = y + dy, x + dx
        if grid[y][x] != 0:
            bids.append(grid[y][x])
        bidpos[y][x] = i
        i += 1
    if d % 2 == 1:
        diff += 1
    d = (d + 1) % 4
score = 0
for d, s in cmd:
    y, x = sy, sx
    dy, dx = dirs[d]
    for _ in range(s):
        y, x = y + dy, x + dx
        if bidpos[y][x] > len(bids) - 1: continue
        bids[bidpos[y][x]] = -1
    bids = [b for b in bids if b != -1]
    flag = True
    while flag:
        flag = False
        last = 0
        for i in range(1, len(bids) + 1):
            if i < len(bids) and bids[i-1] == bids[i]:
                continue
            cnt = i - last
            if cnt >= 4:
                score += bids[last] * cnt
                for idx in range(last, i):
                    bids[idx] = -1
                flag = True
            last = i
        bids = [b for b in bids if b != -1]
    groups = []
    for b in bids:
        if not groups:
            groups.append([b, 1])
            continue
        if groups[-1][0] == b:
            groups[-1][1] += 1
        else:
            groups.append([b, 1])
    bids = []
    for b, c in groups:
        bids.extend([c, b])
        if len(bids) >= n * n - 1: break
    y, x = sy, sx
    diff, d = 1, 0
print(score)