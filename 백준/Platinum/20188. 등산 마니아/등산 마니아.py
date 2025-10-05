import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
con = [[] for _ in range(n+1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    con[a].append((i, b))
    con[b].append((i, a))
root = (1, -1, [])
def contree(node: tuple[int, int, list] = root):
    v, p, ch = node
    for i, nv in con[v]:
        if nv == p: continue
        newnode = (nv, v, [])
        contree(newnode)
        ch.append((i, newnode))
    node = v, p, ch
paths = [[] for _ in range(n+1)]
def findpaths(node: tuple[int, int, list] = root, path: list = []):
    paths[node[0]] = path
    for e, nnode in node[2]:
        findpaths(nnode, path + [e])
contree()
findpaths()
paths = [set(p) for p in paths]
result = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        result += len(paths[i] | paths[j])
print(result)