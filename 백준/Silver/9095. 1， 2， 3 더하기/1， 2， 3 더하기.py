t = int(input())
inputs = [int(input()) for _ in range(t)]
memo = [0] * (max(max(inputs), 4) + 1)
memo[1] = 1
memo[2] = 2
memo[3] = 4
def dp(n):
    if memo[n]:
        return memo[n]
    for i in range(1, 4):
        memo[n] += dp(n - i)
    return memo[n]
for n in inputs:
    print(dp(n))

