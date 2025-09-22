def findmax(n):
    ans = ""
    if n % 2 == 1:
        ans += "7" if n % 2 == 1 else ""
        n -= 3
    return ans + "1" * (n // 2)
best = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}
dp = [1e51] * 101
for b in best:
    dp[b] = best[b]
dp[6] = 6
def findmin(n):
    if n < 2: return 1e51
    if dp[n] != 1e51: return dp[n]
    for b in best:
        leftmin = findmin(n - b)
        dp[n] = min(dp[n], leftmin * 10 + best[b])
    return dp[n]
t = int(input())
for _ in range(t):
    n = int(input())
    print(findmin(n), findmax(n))