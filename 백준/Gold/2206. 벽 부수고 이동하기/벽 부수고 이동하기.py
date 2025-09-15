from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
q = deque([(0, 0, 1, 0)])
INF = n * m * 2
dist = [[ [INF, INF] for _ in range(m) ] for _ in range(n)]
dist[0][0][0] = 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while q:
    y, x, d, broken = q.popleft()
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if grid[ny][nx] == 0 and dist[ny][nx][broken] > d + 1:
                    dist[ny][nx][broken] = d + 1
                    q.append((ny, nx, d + 1, broken))
            elif grid[ny][nx] == 1 and broken == 0 and dist[ny][nx][1] > d + 1:
                 dist[ny][nx][1] = d + 1
                 q.append((ny, nx, d + 1, 1))
res = min(dist[n-1][m-1])
print(res if res != INF else -1)