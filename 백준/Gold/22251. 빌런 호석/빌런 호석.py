ssd = [0b1110111, 0b0010010, 0b1011101,\
       0b1011011, 0b0111010, 0b1101011,\
        0b1101111, 0b1010010, 0b1111111,\
            0b1111011]
ssds = [[bin(x^y).count('1') for x in ssd] for y in ssd]
n, k, p, x = map(int, input().split())
sx = str(x)
if k > len(sx):
    sx = "0" * (k - len(sx)) + sx
def brute(i: int = 0, left: int = p, cur: str = sx):
    if i == len(sx):
        icur = int(cur)
        if icur == x: return 0
        if 1 <= icur <= n: return 1
        return 0
    total = 0
    ch = int(cur[i])
    for k in range(10):
        nleft = left - ssds[ch][k]
        if nleft < 0: continue
        ncur = cur[:i] + str(k) + cur[i+1:]
        total += brute(i+1, nleft, ncur)
    return total
print(brute())