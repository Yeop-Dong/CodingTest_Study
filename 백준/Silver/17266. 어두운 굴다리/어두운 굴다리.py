n = int(input())
m = int(input())
lights = list(map(int, input().split()))

l, r = 0, n
best = n
while l <= r:
    mid = (l + r) // 2
    if lights[0] - mid > 0 or lights[-1] + mid < n:
        l = mid + 1
        continue
    for i in range(m - 1):
        if lights[i] + mid < lights[i+1] - mid:
            break
    else:
        best = mid
        r = mid - 1
        continue
    l = mid+1
    continue
print(best)