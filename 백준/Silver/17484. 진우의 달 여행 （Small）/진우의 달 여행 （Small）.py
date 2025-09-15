from collections import deque
n, m = map(int, input().split())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
dirs = [-1, 0, 1]
limit = n * m * 100 + 1
best = [ [[  cost[0][j] for _ in dirs ] for j in range(m)] ]
best += [ [ [  limit for _ in dirs ] for _ in range(m) ] for _ in range(1, n) ]
for i in range(n):
    for j in range(m):
        for k in range(3):
            if j == 0 and k == 2 or j == m -1 and k == 0:
                continue
            for l in range(3):
                if k == l:
                    continue
                best[i][j][k] = min(best[i][j][k], best[i-1][j-k+1][l] + cost[i][j])
best = min(map(min, best[-1]))
print(best)