from collections import defaultdict
n, d, k, c = map(int, input().split())
sushi = [ int(input()) for _ in range(n) ]
sushi += sushi[:k - 1]
kind = defaultdict(int)
l, r = 0, k - 1
kind[c] += 1
for i in range(0, k):
    kind[sushi[i]] += 1
best = len(kind)
for _ in range(n - 1):
    kind[sushi[l]] -= 1
    if kind[sushi[l]] == 0:
        kind.pop(sushi[l])
    l += 1
    r += 1
    kind[sushi[r]] += 1
    best = max(best, len(kind))
print(best)