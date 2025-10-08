from collections import deque
n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
ctrls = deque([])
for _ in range(l):
    x, c = input().split()
    c = -1 if c == 'L' else 1
    ctrls.append((int(x), c))
snake = [(1, 1)]
headto = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
t = 1
while True:
    y, x = snake[-1]
    dy, dx = dirs[headto]
    ny, nx = y + dy, x + dx
    if ny < 1 or ny > n or nx < 1 or nx > n: break
    if (ny, nx) in snake: break
    snake.append((ny, nx))
    if (ny, nx) in apples:
        apples.remove((ny, nx))
    else:
        snake.pop(0)
    if ctrls and ctrls[0][0] == t:
        headto = (headto + ctrls[0][1]) % 4
        ctrls.popleft()
    t += 1
print(t)