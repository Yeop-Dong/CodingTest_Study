n = int(input())
heights = []
for _ in range(n):
    x, y = map(int, input().split())
    heights.append((x, y))
heights.sort(key = lambda x: x[0])
mx, my = max(heights, key=lambda x: x[1])
flag = False
curh = 0
area = 0
for i in range(n - 1):
    x1, y1 = heights[i]
    x2, y2 = heights[i+1]
    if mx == x1:
        break
    curh = max(curh, y1)
    area += (x2 - x1) * curh
curh = 0
for i in range(n - 1, 0, -1):
    x1, y1 = heights[i]
    x2, y2 = heights[i-1]
    if mx == x1:
        break
    curh = max(curh, y1)
    area += (x1 - x2) * curh
area += my
print(area)