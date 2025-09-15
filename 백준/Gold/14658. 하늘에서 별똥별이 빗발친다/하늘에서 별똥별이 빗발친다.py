import sys
input = lambda: sys.stdin.readline().rstrip()
n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]
deflect = 0
for x1, _ in stars:
    for _, y1 in stars:
        x2 = x1 + l
        y2 = y1 + l
        cnt = 0
        for ix, iy in stars:
            if x1 <= ix <= x2 and y1 <= iy <= y2:
                cnt += 1
        deflect = max(deflect, cnt)
print(k - deflect)