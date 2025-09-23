import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = grid[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i-1] + grid[0][i]
for i in range(1, n):
    l, r = [0] * m, [0] * m
    up = [dp[i-1][j] + grid[i][j] for j in range(m)]
    l[0] = up[0]
    for j in range(1, m):
        l[j] = max(up[j], l[j-1] + grid[i][j])
    r[-1] = up[-1]
    for j in range(m - 2, -1, -1):
        r[j] = max(up[j], r[j+1] + grid[i][j])
    for j in range(m):
        dp[i][j] = max(l[j], r[j])
print(dp[-1][-1])
