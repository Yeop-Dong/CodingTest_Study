import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
spread = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)
field = [[5] * n for _ in range(n)]
for _ in range(k):
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            alive, food = deque(), 0
            while trees[i][j]:
                age = trees[i][j].popleft()
                if field[i][j] >= age:
                    field[i][j] -= age
                    alive.append(age + 1)
                else:
                    food += age // 2
            trees[i][j] = alive
            field[i][j] += food
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dx, dy in spread:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            trees[ni][nj].appendleft(1)
    for i in range(n):
        for j in range(n):
            field[i][j] += a[i][j]    
print(sum(len(trees[i][j]) for i in range(n) for j in range(n)))
