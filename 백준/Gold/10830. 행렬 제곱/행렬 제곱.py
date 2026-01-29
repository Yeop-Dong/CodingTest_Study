n, b = map(int, input().split())
mod = 1000
arr = [ list(map(int, input().split())) for _ in range(n) ]
def mul(x, y):
    z = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i][j] += x[i][k] * y[k][j]
            z[i][j] %= mod
    return z
def effpow(arr, eff):
    if eff == 1:
        return arr
    if eff % 2 == 0:
        res = effpow(arr, eff // 2)
        return mul(res, res)
    res = effpow(arr, (eff - 1) // 2)
    return mul(arr, mul(res, res))
arr = [[ cell % mod for cell in row] for row in arr]
for row in effpow(arr, b):
    print(*row)