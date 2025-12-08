from collections import deque
dice = [2,1,5,6,4,3]
rollinfo = [
    [0, 4, 2, 5, 3, 1], #E
    [3, 0, 1, 2, 4, 5], #S
    [0, 5, 2, 4, 1, 3], #W
    [1, 2, 3, 0, 4, 5], #N
]
rev = [2, 3, 0, 1]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] #ESWN
d = 0 #E
roll = lambda: [dice[rollinfo[d][i]] for i in range(6)]
face = lambda: dice[3]
rotate = lambda clockwise: (d + (1 if clockwise else -1)) % 4
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
y, x = 0, 0
score = 0
for _ in range(k):
    dy, dx = delta[d]
    ny, nx = y + dy, x + dx
    if not (0 <= ny < n and 0 <= nx < m):
        d = rev[d]
        dy, dx = delta[d]
        ny, nx = y + dy, x + dx
    y, x = ny, nx
    dice = roll()
    a, b = face(), grid[y][x]
    q = deque([(y, x)])
    visited = set()
    visited.add((y, x))
    c = 1
    while q:
        ty, tx = q.popleft()
        for dy, dx in delta:
            ny, nx = ty + dy, tx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) not in visited and grid[ny][nx] == b:
                    visited.add((ny, nx))
                    c += 1
                    q.append((ny, nx))
    score += b * c
    if a > b: d = rotate(True)
    elif a < b: d = rotate(False)
print(score)
