n = int(input())
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
grid = [[False] * 101 for _ in range(101)]

def dragon(d, g, curve = []):
    if g == -1:
        return curve
    if not curve:
        curve = [d]
        return dragon(d, g - 1, curve)
    ncurve = []
    for c in reversed(curve):
        nc = (c + 1) % 4
        ncurve.append(nc)
    return dragon(d, g - 1, curve + ncurve)
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve = dragon(d, g)
    grid[y][x] = True
    for c in curve:
        dy, dx = dirs[c]
        y, x = y + dy, x + dx
        grid[y][x] = True
cnt = 0
for y in range(100):
    for x in range(100):
        if all([grid[y][x], grid[y+1][x], grid[y][x+1], grid[y+1][x+1]]):
            cnt += 1
print(cnt)
