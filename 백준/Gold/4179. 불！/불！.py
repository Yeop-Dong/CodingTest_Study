from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
INF = 1000001
fire = [[INF] * c for _ in range(r)]
jh = [[INF] * c for _ in range(r)]
fq = deque([(i, j) for i in range(r) for j in range(c) if grid[i][j] == 'F'])
jq = deque([(i, j) for i in range(r) for j in range(c) if grid[i][j] == 'J'])
for y, x in fq: fire[y][x] = 0
for y, x in jq: jh[y][x] = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
border_chk = lambda y, x: 0 <= y < r and 0 <= x < c
while fq:
    y, x = fq.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if border_chk(ny, nx) and fire[ny][nx] == INF and grid[ny][nx] != '#':
            fire[ny][nx] = fire[y][x] + 1
            fq.append((ny, nx))
ans = "IMPOSSIBLE"
while jq:
    y, x = jq.popleft()
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not border_chk(ny, nx):
            ans = jh[y][x] + 1
            jq.clear()
            break
        if border_chk(ny, nx) and jh[ny][nx] == INF and grid[ny][nx] != '#':
            if fire[ny][nx] > jh[y][x] + 1:
                jh[ny][nx] = jh[y][x] + 1
                jq.append((ny, nx))
print(ans)