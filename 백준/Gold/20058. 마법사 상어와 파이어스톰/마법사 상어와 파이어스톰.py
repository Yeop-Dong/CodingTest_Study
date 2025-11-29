import sys
sys.setrecursionlimit(10**6)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
input = lambda: sys.stdin.readline().rstrip()
n, q = map(int, input().split())
n = 2 ** n
a = [list(map(int, input().split())) for _ in range(n)]
l = list(map(lambda x: 2 ** int(x), input().split()))
def firestorm(li):
    tmp = [[0] * li for _ in range(li)]
    for r in range(0, n, li):
        for c in range(0, n, li):
            for i in range(li):
                for j in range(li):
                    tmp[i][j] = a[r + li - 1 - j][c + i]
            for i in range(li):
                for j in range(li):
                    a[r+i][c+j] = tmp[i][j]
    decrease = []
    for r in range(n):
        for c in range(n):
            if a[r][c] == 0: continue
            noice = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n and a[nr][nc] != 0):
                    noice += 1
                    if noice == 2:
                        break
            else:
                continue
            decrease.append((r, c))
    for r, c in decrease:
        a[r][c] -= 1
def dfs(r, c):
    visited[r][c] = True
    result = 1
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and a[nr][nc] != 0:
            result += dfs(nr, nc)
    return result
for li in l:
    firestorm(li)
print(sum(map(sum, a)))
visited = [[False] * n for _ in range(n)]
big = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c] and a[r][c] != 0:
            big = max(big, dfs(r, c))
print(big)
