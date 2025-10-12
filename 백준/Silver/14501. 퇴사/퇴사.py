import sys
sys.setrecursionlimit(10**6)
n = int(input())
tp = [ list(map(int, input().split())) for _ in range(n) ]
for i in range(n):
    if tp[i][0] + i > n:
        tp[i][1] = 0
dp = [0] * n
def dfs(k):
    if k >= n:
        return 0
    if dp[k]:
        return dp[k]
    pick = tp[k][1] + dfs(k + tp[k][0])
    notpick = dfs(k + 1)
    dp[k] = max(pick, notpick)
    return dp[k]
dfs(0)
print(dp[0])