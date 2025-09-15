import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().rstrip()
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
l, r = 1, house[-1] - house[0]
best = 0
while l <= r:
    mid = (l + r) // 2
    cur, cnt = house[0] + mid, 1
    for i in range(1, n):
        if house[i] >= cur:
            cnt += 1
            cur = house[i] + mid
    if cnt >= c:
        best = mid
        l = mid + 1
    else:
        r = mid - 1
print(best)