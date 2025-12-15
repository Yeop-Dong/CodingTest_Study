from collections import deque
m, s = map(int, input().split())
fdir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
sdir = [(-1,0),(0,-1),(1,0),(0,1)]
f = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
def pgrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='\t')
        print()
    print()
offset = lambda idx: int(idx) - 1
for _ in range(m):
    fx, fy, d = map(offset, input().split())
    f[fx][fy].append(d)
sx, sy = map(offset, input().split())
for _ in range(s):
    mf = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in f[x][y]:
                tx, ty = x, y
                for _ in range(8):
                    dx, dy = fdir[d]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and \
                    smell[nx][ny] == 0 and (sx, sy) != (nx, ny):
                        tx, ty = nx, ny
                        break
                    d = (d - 1) % 8
                mf[tx][ty].append(d)
    # pgrid(mf)
    # pgrid(smell)
    q = deque([(sx, sy, 0, [])])
    bcnt, bhist = -1, []
    while q:
        x, y, cnt, hist = q.popleft()
        for d in range(4):
            dx, dy = sdir[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                ncnt = cnt
                if (nx, ny) not in hist:
                    ncnt += len(mf[nx][ny])
                nhist = hist + [(nx, ny)]
                if len(nhist) == 3:
                    if ncnt > bcnt:
                        # print(ncnt, nhist)
                        bcnt, bhist = ncnt, nhist
                    continue
                q.append((nx, ny, ncnt, nhist))
    sx, sy = bhist[-1]
    # print(bhist)
    for x, y in bhist:
        if mf[x][y]:
            smell[x][y] = 3
            mf[x][y] = []
    # pgrid(mf)
    # pgrid(smell)
    for x in range(4):
        for y in range(4):
            f[x][y].extend(mf[x][y])
            if smell[x][y] > 0:
                smell[x][y] -= 1
    # pgrid(f)
    # pgrid(smell)
result = sum(sum(map(len, row)) for row in f)
print(result)
            


