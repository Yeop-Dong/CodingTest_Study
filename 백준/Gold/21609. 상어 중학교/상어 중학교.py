import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
adjs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
def dfs(grid, visited, i, j, val):
    visited[i][j] = True
    normal, rainbow = [], []
    if grid[i][j] == val: normal.append((i, j))
    else: rainbow.append((i, j))
    for di, dj in adjs:
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n): continue
        if not visited[ni][nj] and grid[ni][nj] in (val, 0):
            nadd, radd = dfs(grid, visited, ni, nj, val)
            normal += nadd
            rainbow += radd
    return normal, rainbow
def grav(grid):
    for j in range(n):
        for i in range(n-1, -1, -1):
            if grid[i][j] == -1 or grid[i][j] is None:
                continue
            k = i + 1
            while k < n:
                if grid[k][j] is not None:
                    break
                k += 1
            if k - 1 != i:
                grid[k-1][j] = grid[i][j]
                grid[i][j] = None
def rotate(grid):
    ngrid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ngrid[n - 1 - j][i] = grid[i][j]
    return ngrid
score = 0
while True:
    rainbows = [(r,c) for c in range(n) for r in range(n) if grid[r][c] == 0]
    visited = [[False] * n for _ in range(n)]
    best, brainbow = [], 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] is not None and grid[i][j] > 0 and not visited[i][j]:
                normal, rainbow = dfs(grid, visited, i, j, grid[i][j])
                total = normal + rainbow
                if len(total) < 2: continue
                if len(total) > len(best) or (len(total) == len(best) and len(rainbow) >= brainbow):
                    best, brainbow = total, len(rainbow)
                for r, c in rainbow:
                    visited[r][c] = False
    if not best:
        break
    for r, c in best:
        grid[r][c] = None
    score += len(best) ** 2
    grav(grid)
    grid = rotate(grid)
    grav(grid)

print(score)