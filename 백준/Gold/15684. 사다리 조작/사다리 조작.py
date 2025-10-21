n, m, h = map(int, input().split())
link = [[False] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    link[a][b] = True
def chkres():
    for i in range(1, n+1):
        pos = i
        cur = 1
        while cur <= h:
            if link[cur][pos]:
                pos += 1
            elif link[cur][pos - 1]:
                pos -= 1
            cur += 1
        if pos != i:
            return False
    return True
ans = 4
def dfs(cnt, sy, sx):
    global ans
    if cnt >= ans:
        return
    if chkres():
        ans = cnt
        return
    if cnt == 3:
        return
    for y in range(sy, h + 1):
        for x in range(sx, n):
            if link[y][x] or link[y][x-1] or link[y][x+1]:
                continue
            link[y][x] = True
            dfs(cnt + 1, y, x + 2)
            link[y][x] = False
        sx = 1
dfs(0, 1, 1)
print(ans if ans < 4 else -1)