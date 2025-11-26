import sys
input = lambda: sys.stdin.readline().rstrip()
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
SPREAD = [
    [(-1,0,7),(1,0,7),(-1,-1,10),(1,-1,10),(-1,1,1),(1,1,1),(0,-2,5),(-2,0,2),(2,0,2)],
    [(0,-1,7),(0,1,7),(1,-1,10),(1,1,10),(-1,-1,1),(-1,1,1),(2,0,5),(0,-2,2),(0,2,2)],
    [(-1,0,7),(1,0,7),(-1,1,10),(1,1,10),(-1,-1,1),(1,-1,1),(0,2,5),(-2,0,2),(2,0,2)],
    [(0,-1,7),(0,1,7),(-1,-1,10),(-1,1,10),(1,-1,1),(1,1,1),(-2,0,5),(0,-2,2),(0,2,2)]
]
ALPHA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
diff, dir = 1, 0
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r = c = n // 2
move = 0
out = 0
while not (r == 0 and c == 0):
    dr, dc = DIRS[dir]
    r, c = r + dr, c + dc
    y = grid[r][c]
    for dr, dc, per in SPREAD[dir]:
        sr, sc = r + dr, c + dc
        cur = y * per // 100
        if 0 <= sr < n and 0 <= sc < n:
            grid[sr][sc] += cur
        else:
            out += cur
        grid[r][c] -= cur
    dr, dc = ALPHA[dir]
    ar, ac = r + dr, c + dc
    if 0 <= ar < n and 0 <= ac <n:
        grid[ar][ac] += grid[r][c]  
    else:
        out += grid[r][c]
    grid[r][c] = 0
    move += 1
    if move == diff:
        if dir == 1 or dir == 3:
            diff += 1
        dir = (dir + 1) % 4
        move = 0
print(out)