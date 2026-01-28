import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
spread = [(0, 1), (0, -1), (1, 0), (-1, 0)]
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
idx = lambda i, j: i * c + j 
parent, swan, water = list(range(r*c)), [], deque()
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'L':
            swan.append((i, j))
            grid[i][j] = '.'
        if grid[i][j] == '.':
            water.append((i, j))
s1, s2 = swan[0], swan[1]
def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]
def union(i, j):
    ri = find(i)
    rj = find(j)
    if ri != rj:
        parent[rj] = ri
day = -1
visited = [[False] * c for _ in range(r)]
while find(idx(*s1)) != find(idx(*s2)):
    for _ in range(len(water)):
        y, x = water.popleft()
        grid[y][x] = '.'
        for dy, dx in spread:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c:
                if grid[ny][nx] == '.':
                    union(idx(y, x), idx(ny, nx))
                elif grid[ny][nx] == 'X' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    water.append((ny, nx))
        
    day += 1
print(day)
