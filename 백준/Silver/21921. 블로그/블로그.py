n, x = map(int, input().split())
visitor = list(map(int, input().split()))
for i in range(n - 1):
    visitor[i+1] += visitor[i]
visitor = [0] + visitor
most, same = 0, 0
for i in range(x, n+1):
    cur = visitor[i] - visitor[i - x]
    if most < cur:
        most = cur
        same = 1
    elif most == cur:
        same += 1
if most == 0:
    print("SAD")
else:
    print(most)
    print(same)