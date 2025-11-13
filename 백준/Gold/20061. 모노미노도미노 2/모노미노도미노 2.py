n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
b, g = [[0]*4 for _ in range(10)], [[0]*4 for _ in range(10)]
score = 0
def drop(grid, blk):
    while True:
        if any(x + 1 >= 10 or grid[x + 1][y] for x, y in blk):
            break
        blk = [(x + 1, y) for x, y in blk]
    for x, y in blk:
        grid[x][y] = 1
def collapse(grid, row):
    for r in range(row, 4, -1):
        grid[r] = grid[r - 1][:]
    grid[4] = [0] * 4
def chk(grid):
    cnt = 0
    while True:
        full = [x for x in range(6, 10) if all(grid[x][y] == 1 for y in range(4))]
        if not full:
            break
        for x in full:
            collapse(grid, x)
        cnt += len(full)
    row = sum(1 if any(grid[x][y] for y in range(4)) else 0 for x in range(4, 6))
    for _ in range(row):
        collapse(grid, 9)
    grid[4], grid[5] = [0] * 4, [0] * 4
    return cnt
for t, x, y in info:
    gblk = [(x, y)]
    if t == 2: gblk.append((x, y + 1))
    elif t == 3: gblk.append((x + 1, y))
    bblk = [(y, x) for x, y in gblk]
    drop(g, gblk)
    drop(b, bblk)
    score += chk(g)
    score += chk(b)
left = sum(row.count(1) for row in g[6:])
left += sum(row.count(1) for row in b[6:])
print(score)
print(left)
