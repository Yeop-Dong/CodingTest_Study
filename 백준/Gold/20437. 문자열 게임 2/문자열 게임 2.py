from collections import defaultdict
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    m, M = 10001, 0
    chars = defaultdict(list)
    for i, c in enumerate(w):
        chars[c].append(i)
    for c in chars:
        l = chars[c]
        for i in range(len(l) - k + 1):
            cur = l[i+k-1] - l[i] + 1
            m = min(m, cur)
            M = max(M, cur)
    if m == 10001:
        print(-1)
    else:
        print(m, M)