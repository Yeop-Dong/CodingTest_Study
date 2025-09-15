import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
n, m = int(input()), int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
plan = [p - 1 for p in plan]
parent = [i for i in range(n)]
def find(x):
    if x == parent[x]: return x
    else: parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x, y = find(x), find(y)
    if y < x: parent[x] = y
    else: parent[y] = x
visited = [False] * n
def dfs(v, parent = None):
    visited[v] = True
    if parent is not None:
        union(v, parent)
    for i in range(n):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i, v)
for i in range(n):
    if not visited[i]:
        dfs(i)
yesorno = True
for i in range(len(plan) - 1):
    if find(plan[i]) != find(plan[i+1]):
        yesorno = False
        break
print("YES" if yesorno else "NO")