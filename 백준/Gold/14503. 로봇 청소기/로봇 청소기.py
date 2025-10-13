from enum import Enum
class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3
rotate = { Dir.E: Dir.N, Dir.N: Dir.W,
           Dir.W: Dir.S, Dir.S: Dir.E}
reverse = { Dir.E: Dir.W, Dir.N: Dir.S,
            Dir.W: Dir.E, Dir.S: Dir.N }
move = { Dir.E: (0, 1), Dir.N: (-1, 0),
        Dir.W: (0, -1), Dir.S: (1, 0)}
n, m = map(int, input().split())
r, c, d = map(int, input().split())
d = Dir(d)
grid = [ list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    if grid[r][c] == 0:
        grid[r][c] = 2
        cnt += 1
    for _ in range(4):
        d = rotate[d]
        dr, dc = move[d]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == 0:
            r, c = nr, nc
            break
    else:
        td = reverse[d]
        dr, dc = move[td]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] == 1:
            break
        r, c = nr, nc
print(cnt)