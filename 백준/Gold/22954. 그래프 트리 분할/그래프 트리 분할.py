import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(1, m+1):
    u, v = map(int, input().split())
    g[u].append((i, v))
    g[v].append((i, u))
if n <= 2 or m < n - 2:
    print(-1)
    exit()
visited = [False] * (n+1)
def dfs(v, nodes: list, edges: list):
    visited[v] = True
    nodes.append(v)
    for e, nv in g[v]:
        if not visited[nv]:
            edges.append(e)
            dfs(nv, nodes, edges)
    return nodes, edges
comps = []
for i in range(1, n+1):
    if not visited[i]:
        comps.append(dfs(i, [], []))
if len(comps) > 2:
    print(-1)
    exit()
if len(comps) == 2:
    if len(comps[0][0]) == len(comps[1][0]):
        print(-1)
        exit()
    print(len(comps[0][0]), len(comps[1][0]))
    print(*comps[0][0])
    print(*comps[0][1])
    print(*comps[1][0])
    print(*comps[1][1])
    exit()

leaf = comps[0][0][-1]
comps[0][0].remove(leaf)
eleaf = []
for i, nxt in g[leaf]:
    eleaf.append(i)
print(len(comps[0][0]), 1)
print(*comps[0][0])
print(*[ i for i in comps[0][1] if i not in eleaf ])
print(leaf)
print()
