from collections import defaultdict
n = int(input())
g = defaultdict(int)
for i in range(1, n+1):
    g[i] = int(input())
cycle = set()
def dfs(v: int) -> bool:
    visited[v] = True
    nxt = g[v]
    if not visited[nxt]:
        dfs(nxt)
    elif not finished[nxt]:
        cycle.add(nxt)
    finished[v] = True
for i in range(1, n+1):
    visited, finished = [False] * (n+1), [False] * (n+1)
    dfs(i)
cycle = sorted(list(cycle))
print(len(cycle))
for c in cycle:
    print(c)