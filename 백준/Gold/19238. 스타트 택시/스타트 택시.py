import sys
from collections import deque
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
input = lambda: sys.stdin.readline().rstrip()
n, m, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
y, x = map(lambda x: int(x) - 1, input().split())
psngrs = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
sgrid, egrid = [[-1]*n for _ in range(n)], [[-1]*n for _ in range(n)]
for idx, (i, j, k, l) in enumerate(psngrs):
    sgrid[i][j] = idx
    egrid[k][l] = idx
def bfs(sy, sx, end = -1):
    visited = [[False] * n for _ in range(n)]
    visited[sy][sx] = True
    dist = float('inf')
    cand = []
    q = deque([(sy, sx, 0)])
    while q:
        i, j, d = q.popleft()
        if d > dist:
            break
        if end == -1 and sgrid[i][j] != -1:
            cand.append((i, j, d))
            dist = d
            continue
        if end != -1 and egrid[i][j] == end:
            return (i, j, d)
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] != 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj, d+1))
    if end == -1 and cand:
        cand.sort(key=lambda x: (x[2], x[0], x[1]))
        return cand[0]
    return (-1, -1, -1)
pcount = len(psngrs)
while pcount > 0:
    sy, sx, sd = bfs(y, x)
    if sy == -1 or fuel < sd: break
    fuel -= sd
    num = sgrid[sy][sx]
    _, _, ey, ex = psngrs[num]
    egrid[ey][ex] = num
    ey, ex, ed = bfs(sy, sx, num)
    if ey == -1 or fuel < ed: break
    fuel += ed
    sgrid[sy][sx] = egrid[ey][ex] = -1
    pcount -= 1
    y, x = ey, ex
if pcount > 0:
    print("-1")
else:
    print(fuel)