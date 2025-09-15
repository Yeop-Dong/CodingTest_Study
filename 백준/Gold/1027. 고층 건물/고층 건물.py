n = int(input())
h = list(map(int, input().split()))
best = 0
for x, y in enumerate(h):
    regmin, regmax = None, None
    visible = 0
    for lx in range(x - 1, -1, -1):
        ly = h[lx]
        slope = (y - ly) / (x - lx)
        if regmin is None or regmin > slope:
            regmin = slope
            visible += 1
    for rx in range(x + 1, n):
        ry = h[rx]
        slope = (ry - y) / (rx - x)
        if regmax is None or regmax < slope:
            regmax = slope
            visible += 1
    best = max(best, visible)
print(best)