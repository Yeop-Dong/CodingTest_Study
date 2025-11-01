import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
r, c, m = map(int, input().split())
ICYCLE, JCYCLE = (r - 1) * 2, (c - 1) * 2
sharks = [tuple(map(int, input().split())) for _ in range(m)]
sharks = [(i-1, j-1, s, d, z) for (i,j,s,d,z) in sharks]
grid = [[None] * c for _ in range(r)]
for i, j, s, d, z in sharks:
    grid[i][j] = (s, d, z)
total = 0
for king in range(c):
    fished = False
    ngrid = [[None] * c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            if grid[i][j]:
                s, d, z = grid[i][j]
                if not fished and j == king:
                    total += grid[i][j][2]
                    fished = True
                    continue
                ni, nj = i, j
                if d in (1, 2):
                    ni = s + ICYCLE - i if d == 1 else i + s
                    ni %= ICYCLE
                    if ni >= r: 
                        ni = ICYCLE - ni
                        d = 1
                    else:
                        d = 2
                else:
                    nj = s + JCYCLE - j if d == 4 else j + s
                    nj %= JCYCLE
                    if nj >= c: 
                        nj = JCYCLE - nj
                        d = 4
                    else:
                        d = 3
                if ngrid[ni][nj] and ngrid[ni][nj][2] > z:
                    continue
                ngrid[ni][nj] = (s, d, z)
    grid = ngrid
print(total)