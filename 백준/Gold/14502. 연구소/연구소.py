from itertools import combinations
from collections import deque
n, m = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
virus, wall, empty = [], [], []
for y in range(n):
    for x in range(m):
        if grid[y][x] == 2:
            virus.append((y, x))
        elif grid[y][x] == 1:
            wall.append((y, x))
        else:
            empty.append((y, x))
def safearea(grid: list[list[int]], pick: tuple[int, int, int]):
    for p in pick:
        i, j = empty[p]
        grid[i][j] = 1
    for v in virus:
        q = deque([v])
        while q:
            y, x = q.popleft()
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if grid[ny][nx] == 0:
                        grid[ny][nx] = 2
                        q.append((ny, nx))
    cnt = 0
    for i, j in empty:
        if grid[i][j] == 0:
            cnt += 1
        else:
            grid[i][j] = 0
    return cnt
eP3 = list(combinations(range(len(empty)), 3))
best = 0
for p in eP3:
    best = max(best, safearea(grid, p))
print(best)