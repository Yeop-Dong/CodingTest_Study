import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def dfs(y, x):
    visited[y][x] = True
    population = nations[y][x]
    union = [(y, x)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            popgap = abs(nations[ny][nx] - nations[y][x])
            if not visited[ny][nx] and l <= popgap <= r:
                npop, nunion = dfs(ny, nx)
                population += npop
                union += nunion
    return population, union
cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    unioncnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                population, union = dfs(i, j)
                avgpop = population // len(union)
                for uy, ux in union:
                    nations[uy][ux] = avgpop
                unioncnt += 1
    if unioncnt == n * n:
        break
    cnt += 1
    if unioncnt == 1:
        break
print(cnt)