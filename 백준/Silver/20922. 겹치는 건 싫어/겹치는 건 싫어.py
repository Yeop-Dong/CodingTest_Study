import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
seq = list(map(int, input().split()))
subseq = deque()
cnt = defaultdict(int)
best = 0
for c in seq:
    subseq.append(c)
    cnt[c] += 1
    while cnt[c] > k:
        popped = subseq.popleft()
        cnt[popped] -= 1
    best = max(best, len(subseq))
print(best)