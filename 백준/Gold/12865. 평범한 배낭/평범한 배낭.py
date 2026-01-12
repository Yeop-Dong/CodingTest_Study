n, k = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(1, k+1):
        if things[i-1][0] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - things[i-1][0]] + things[i-1][1])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n][k])