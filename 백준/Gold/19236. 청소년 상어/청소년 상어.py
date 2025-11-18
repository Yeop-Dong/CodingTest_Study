import copy
grid = []
fish = [None] * 17
dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
for y in range(4):
    tmp = []
    row = list(map(int, input().split()))
    for i in range(0, len(row), 2):
        fish[row[i]] = (y, i // 2, row[i+1] - 1)
        tmp.append(row[i])
    grid.append(tmp)
first = grid[0][0]
shark = fish[first]
fish[first] = None
grid[0][0] = None
def move(fish, grid, shark):
    sy, sx, _ = shark
    for i in range(1, 17):
        if fish[i] is None: continue
        y, x, d = fish[i]
        for _ in range(8):
            dy, dx = dirs[d]
            ny, nx = y + dy, x + dx
            if not (0 <= ny < 4 and 0 <= nx < 4) or (ny, nx) == (sy, sx):
                d = (d + 1) % 8
                continue
            if grid[ny][nx] is None:
                grid[ny][nx], grid[y][x] = i, None
                fish[i] = (ny, nx, d)
            else:
                fidx = grid[ny][nx]
                fish[fidx], fish[i] = (y, x, fish[fidx][2]), (ny, nx, d)
                grid[y][x], grid[ny][nx] = fidx, i
            break

def dfs(shark, fish, grid, total):
    nfish = copy.deepcopy(fish)
    ngrid = copy.deepcopy(grid)
    move(nfish, ngrid, shark)
    
    y, x, d = shark
    dy, dx = dirs[d]
    best = total
    for i in range(1, 4):
        ny, nx = y + i * dy, x + i * dx
        if not (0 <= ny < 4 and 0 <= nx < 4):
            break
        if ngrid[ny][nx] is None:
            continue
        fidx = ngrid[ny][nx]
        nd = nfish[fidx][2]
        ngrid[ny][nx] = None
        saved = nfish[fidx]
        nfish[fidx] = None
        best = max(best, dfs((ny, nx, nd), nfish, ngrid, total+fidx))
        ngrid[ny][nx] = fidx
        nfish[fidx] = saved
    return best
best = dfs(shark, fish, grid, first)
print(best)
    
    