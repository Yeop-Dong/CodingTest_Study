import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
P = 0
while True:
    P += 1
    n = int(input())
    if n == 0: break
    c = [list(map(int, input().split())) for _ in range(n)]
    q = deque([(0, 0, c[0][0])])
    dist = [[n * 10] * n for _ in range(n)]
    while q:
        y, x, d = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if dist[ny][nx] > d + c[ny][nx]:
                    dist[ny][nx] = d + c[ny][nx]
                    q.append((ny, nx, dist[ny][nx]))
    print(f"Problem {P}: {dist[n-1][n-1]}")