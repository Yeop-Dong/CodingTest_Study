import sys
input = lambda: sys.stdin.readline().rstrip()
n, s = map(int, input().split())
seq = [0] + list(map(int, input().split()))
n += 1
for i in range(1, n): seq[i] += seq[i-1]
l, r = 0, 1
best = n
while r < n:
    if seq[r] - seq[l] < s:
        r += 1
    else:
        best = min(best, r - l)
        l += 1
print(best if best != n else 0)