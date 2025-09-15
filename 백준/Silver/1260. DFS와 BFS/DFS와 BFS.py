import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write
n, m, v = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    if v1 == v2: continue
    g[v2].append(v1)
for i in g:
    g[i].sort()
sys.setrecursionlimit(10**6)
dfsvisited = [False] * (n + 1)
bfsvisited = [False] * (n + 1)
def dfs(v):
    dfsvisited[v] = True
    print(str(v) + " ")
    for nv in g[v]:
        if dfsvisited[nv]: continue
        dfs(nv)
def bfs(v):
    q = deque([v])
    print(str(v) + " ")
    bfsvisited[v] = True
    while q:
        cur = q.popleft()
        for nv in g[cur]:
            if bfsvisited[nv]: continue
            bfsvisited[nv] = True
            print(str(nv) + " ")
            q.append(nv)
dfs(v)
print("\n")
bfs(v)