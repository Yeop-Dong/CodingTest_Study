import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
sol = list(map(int, input().split()))
l, r = 0, n-1
best, bestl, bestr = abs(sol[l] + sol[r]), l, r
while l < r:
    nsol = sol[l] + sol[r]
    if best > abs(nsol):
        best = abs(nsol)
        bestl = l
        bestr = r
        if best == 0:
            break
    if nsol < 0:
        l += 1
    else:
        r -= 1
print(sol[bestl], sol[bestr])