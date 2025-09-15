import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):
    l, r = 0, n - 1
    while l < r:
        if a[l] + a[r] == a[i]:
            if l == i: l += 1; continue
            if r == i: r -= 1; continue
            cnt += 1; break
        elif a[l] + a[r] < a[i]: l += 1
        else: r -= 1
print(cnt)