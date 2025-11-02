import sys
from itertools import combinations
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
virus = [(i, j) for j in range(n) for i in range(n) if grid[i][j] == 2]
empty = sum(row.count(0) for row in grid)
best = float('inf')
for comb in combinations(virus, m):
    combined = [[float('inf')] * n for _ in range(n)]
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    for y, x in comb:
        q.append((y, x))
        visited[y][x] = 0
    filled = 0
    maxt = 0
    while q:
        y, x = q.popleft()
        t = visited[y][x]
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == -1 and grid[ny][nx] != 1:
                    visited[ny][nx] = t + 1
                    q.append((ny, nx))
                    if grid[ny][nx] == 0:
                        filled += 1
                        maxt = max(maxt, t + 1)
    if filled == empty:
        best = min(best, maxt)
print(best if best != float('inf') else -1)
