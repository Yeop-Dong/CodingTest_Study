# 20:40 시작
import sys
from collections import defaultdict
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(m)]
info = [(r-1, c-1, m, s, d) for r, c, m, s, d in info]
for _ in range(k):
    moved = defaultdict(list)
    for r, c, m, s, d in info:
        dr, dc = dirs[d]
        nr, nc = r + s * dr, c + s * dc
        if nr < 0: nr = n * (-nr // n + 1) + nr
        if nc < 0: nc = n * (-nc // n + 1) + nc
        if nr >= n: nr = nr - n * (nr // n)
        if nc >= n: nc = nc - n * (nc // n)
        moved[(nr, nc)].append((m, s, d))
    ninfo = []
    for r, c in moved:
        cur = moved[(r, c)]
        if len(cur) == 1:
            m, s, d = cur[0]
            ninfo.append((r, c, m, s, d))
            continue
        summ, sums = 0, 0
        even, odd = 0, 0
        for m, s, d in cur:
            summ += m
            sums += s
            if d % 2 == 0: even += 1
            else: odd += 1
        nm = summ // 5
        ns = sums // len(cur)
        if nm == 0: continue
        way = [1, 3, 5, 7]
        if even == 0 or odd == 0:
            way = [0, 2, 4, 6]
        ninfo.extend([(r, c, nm, ns, d) for d in way])
    info = ninfo
print(sum(map(lambda x: x[2], info)))
# 21시 11분 종료