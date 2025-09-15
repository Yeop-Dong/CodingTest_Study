from collections import deque
n, m = map(int, input().split())
ladder = dict([tuple(map(int, input().split())) for _ in range(n)])
snake = dict([tuple(map(int, input().split())) for _ in range(m)])
q = deque([(1, 0)])
best = [101] * 101
best[1] = 0
while q:
    pos, dist = q.popleft()
    for i in range(6, 0, -1):
        npos = pos + i
        if npos > 100:
            continue
        npos = ladder.get(npos, npos)
        npos = snake.get(npos, npos)
        if dist + 1 < best[npos]:
            best[npos] = dist + 1
            q.append((npos, dist + 1))
print(best[100])