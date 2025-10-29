from collections import deque
n = int(input())
space = [ list(map(int, input().split())) for _ in range(n) ]
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
shark = None
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark = (i, j, 2)
            space[i][j] = 0
            break
def bfs(shark):
    sy, sx, size = shark
    dist = [[-1] * n for _ in range(n)]
    dist[sy][sx] = 0
    q = deque([(sy, sx)])
    fish = []
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] == -1:
                if space[ny][nx] <= size:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                    if 0 < space[ny][nx] < size:
                        fish.append((dist[ny][nx], ny, nx))
    if not fish:
        return None           
    return min(fish)

cnt = 0
t = 0
while True:
    res = bfs(shark)
    if not res:
        break
    dist, fy, fx = res
    t += dist
    cnt += 1
    space[fy][fx] = 0
    if cnt == shark[2]:
        shark = (fy, fx, shark[2] + 1)
        cnt = 0
    else:
        shark = (fy, fx, shark[2]) 
print(t)