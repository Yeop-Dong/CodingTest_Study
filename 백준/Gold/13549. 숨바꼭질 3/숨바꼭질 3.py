from collections import deque
n, k = map(int, input().split())
INF = 2 * max(n, k) + 1
visited = [INF] * INF
q = deque([(n, 0)])
visited[n] = 0
valid = lambda x, y: 0 <= x < INF and visited[x] > y
way = [("-1", 1), ("+1", 1), ("*2", 0)]
while q:
    cur, sec = q.popleft()
    for w, cost in way:
        ncur = eval("cur" + w)   
        if valid(ncur, sec + cost):
            visited[ncur] = sec + cost
            q.append((ncur, sec + cost))
print(visited[k])