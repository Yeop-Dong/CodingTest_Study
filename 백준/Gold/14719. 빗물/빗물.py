h, w = map(int, input().split())
blk = list(map(int, input().split()))
left, right = [], []
curmax = 0
for j in range(w):
    left.append(curmax)
    curmax = max(curmax, blk[j])
curmax = 0
for j in range(w -1, -1, -1):
    right.append(curmax)
    curmax = max(curmax, blk[j])
right.reverse()
result = 0
for j in range(w):
    wall = min(left[j], right[j])
    if wall - blk[j] > 0:
        result += wall - blk[j]
print(result)
