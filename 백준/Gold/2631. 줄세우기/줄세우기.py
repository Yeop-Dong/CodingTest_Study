n = int(input())
a = [int(input()) for _ in range(n)]
# find LIS
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))