def accbit(n):
    res = 0
    i = 1
    n += 1
    while i < n:
        k = n // i
        res += k // 2 * i
        if k % 2 == 1:
            res += n % i
        i *= 2
    return res
a, b = map(int, input().split())
print(accbit(b) - accbit(a-1))