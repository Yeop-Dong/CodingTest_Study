from collections import defaultdict, deque
import sys
adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
adjchks = [(0, 0, 1), (1, 0, 0), (0, -1, 1), (0, 0, 0)]
dirs = [[(-1, 1), (0, 1), (1, 1)],
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)]]
chks = [[[(0,0,0), (-1,0,1)], [(0,0,1)], [(1,0,0),(1,0,1)]],
        [[(0,0,0),(-1,-1,1)], [(0,-1,1)], [(1,0,0),(1,-1,1)]],
        [[(0,-1,0),(0,-1,1)], [(0,0,0)], [(0,1,0),(0,0,1)]],
        [[(1,-1,0),(0,-1,1)], [(1,0,0)], [(1,1,0),(0,0,1)]]]
input = lambda: sys.stdin.readline().rstrip()
r, c, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
heaters, inspect = [], []
for i in range(r):
    for j in range(c):
        if 0 < grid[i][j] < 5:
            heaters.append((i, j, grid[i][j] - 1))
        elif grid[i][j] == 5:
            inspect.append((i, j))
temp = [[0] * c for _ in range(r)]
w = int(input())
wall = set()
for _ in range(w):
    x, y, t = map(int, input().split())
    x, y = x - 1, y - 1
    wall.add((x, y, t))
spread = [[0] * c for _ in range(r)]
for x, y, d in heaters:
    delta = dirs[d]
    check = chks[d]
    dx, dy = delta[1]
    x, y = x + dx, y + dy
    if not (0 <= x < r and 0 <= y < c): continue
    visited = set()
    q = deque([(x, y, 5)])
    visited.add((x, y))
    spread[x][y] += 5
    while q:
        x, y, t = q.popleft()
        for i in range(3):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < r and 0 <= ny < c): continue
            if (nx, ny) in visited: continue
            if any((x + dx, y + dy, ver) in wall for dx, dy, ver in check[i]): continue
            visited.add((nx, ny))
            spread[nx][ny] += t - 1
            if t - 1 > 1:
                q.append((nx, ny, t - 1))
chocolate = 0
while True:
    for x in range(r):
        for y in range(c):
            temp[x][y] += spread[x][y]
    add = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if temp[x][y] == 0: continue
            for delta, check in zip(adjs, adjchks):
                dx, dy = delta
                nx, ny = x + dx, y + dy
                dx, dy, ver = check
                cx, cy = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and (cx, cy, ver) not in wall:
                    if temp[nx][ny] < temp[x][y]:
                        div = (temp[x][y] - temp[nx][ny]) // 4
                        add[x][y] -= div
                        add[nx][ny] += div
    for x in range(r):
        for y in range(c):
            temp[x][y] += add[x][y]
            if temp[x][y] < 0:
                temp[x][y] = 0
    for x in range(r):
        if temp[x][0] > 0: temp[x][0] -= 1
        if temp[x][-1] > 0: temp[x][-1] -= 1
    for y in range(1, c - 1):
        if temp[0][y] > 0: temp[0][y] -= 1
        if temp[-1][y] > 0: temp[-1][y] -= 1
    chocolate += 1
    if chocolate > 100:
        break
    if all(temp[x][y] >= k for x, y in inspect):
        break
print(chocolate)