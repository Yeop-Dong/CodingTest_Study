n, d = map(int, input().split())
sh = [ list(map(int, input().split())) for _ in range(n) ]
sh.sort()
dp = [ i for i in range(d+1) ]
k = 0
for i in range(d+1):
    dp[i] = min(dp[i-1] + 1, dp[i])
    while k < n:
        if sh[k][0] != i: break
        if sh[k][1] <= d:
            dp[sh[k][1]] = min(dp[i] + sh[k][2], dp[sh[k][1]])
        k += 1
print(dp[d])