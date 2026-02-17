n = int(input())
nstr = str(n)
nlen = len(nstr)
if nlen == 1:
    print(n)
else:
    total = 0
    mul = 9
    for i in range(1, nlen):
        total += i * mul
        mul *= 10
    total += (n - 10 ** (nlen - 1) + 1) * nlen
    print(total)