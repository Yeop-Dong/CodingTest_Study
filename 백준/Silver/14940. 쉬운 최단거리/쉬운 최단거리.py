import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write
n, m = map(int, input().split())
world = [ list(map(int, input().split())) for _ in range(n) ]
for i, row in enumerate(world):
    for j, data in enumerate(row):
        if data == 2:
            ty, tx = i, j
            break
INF = 1000000000
dist = [ [INF] * m for _ in range(n) ]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque([(ty, tx, 0)])
dist[ty][tx] = 0
while q:
    y, x, d = q.popleft()
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if world[ny][nx] == 1 and dist[ny][nx] > d + 1:
                dist[ny][nx] = d + 1
                q.append((ny, nx, d+1))
for i, row in enumerate(dist):
    for j, data in enumerate(row):
        if world[i][j] == 0:
            print("0 ")
        else:
            print(f"{data if data != INF else -1} ")
    print("\n")