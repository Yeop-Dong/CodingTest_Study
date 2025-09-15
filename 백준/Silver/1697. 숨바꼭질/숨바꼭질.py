from collections import deque
n, k = map(int, input().split())
INF = 100001
visited = [False] * INF
q = deque([(n, 0)])
visited[n] = True
valid = lambda x: 0 <= x < INF and not visited[x]
way = ["-1", "+1", "*2"]
while q:
    cur, sec = q.popleft()
    if cur == k:
        print(sec)
        break
    for w in way:
        ncur = eval("cur" + w)   
        if valid(ncur):
            visited[ncur] = True
            q.append((ncur, sec + 1))