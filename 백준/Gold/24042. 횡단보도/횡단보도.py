import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, i))
    g[b].append((a, i))
INF = int(1e18)
dist = [INF] * n
dist[0] = 0
pq = [(0, 0)]
while pq:
    t, node = heapq.heappop(pq)
    if dist[node] < t: continue
    for nxt, idx in g[node]:
        wait = (idx - t % m + m) % m
        nt = t + wait + 1
        if dist[nxt] > nt:
            dist[nxt] = nt
            heapq.heappush(pq, (nt, nxt))
print(dist[-1])