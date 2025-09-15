import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, w = map(int, input().split())
    g[v1].append((v2, w))
    g[v2].append((v1, w))
hq = [(0, 1)]
visited = set()
dist = [50000 * 1000 + 1] * (n + 1)
dist[1] = 0
while hq:
    _, cur = heapq.heappop(hq)
    if cur in visited: continue
    visited.add(cur)
    for nxt, w in g[cur]:
        if dist[cur] + w < dist[nxt]:
            dist[nxt] = dist[cur] + w
            heapq.heappush(hq, (dist[nxt], nxt))
print(dist[-1])