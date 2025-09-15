import heapq
n, m, x = map(int, input().split())
g1 = {}
g2 = {}
for _ in range(m):
    a, b, t = map(int, input().split())
    g1[a] = g1.get(a, []) + [(b, t)]
    g2[b] = g2.get(b, []) + [(a, t)]
tox = {i: float('inf') for i in range(1, n+1)}
fromx = {i: float('inf') for i in range(1, n+1)}

def dijkstra(graph, dist):
    pq = [(0, x)]
    dist[x] = 0
    while pq:
        time, node = heapq.heappop(pq)
        if dist[node] < time: continue
        for nxt, t in graph.get(node, []):
            if dist[nxt] > time + t:
                dist[nxt] = time + t
                heapq.heappush(pq, (time + t, nxt))
dijkstra(g1, tox)
dijkstra(g2, fromx)
ans = 0
for i in range(1, n+1):
    ans = max(ans, tox[i] + fromx[i])
print(ans)