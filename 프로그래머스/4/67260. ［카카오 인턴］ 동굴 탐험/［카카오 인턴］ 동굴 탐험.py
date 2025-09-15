from collections import deque
import sys
sys.setrecursionlimit(10**6)
def solution(n, path, order):
    g = [ [] for _ in range(n)]
    for v1, v2 in path:
        g[v1].append(v2)
        g[v2].append(v1)
    
    dg = [ [] for _ in range(n) ]
    q = deque([0])
    visited =[False] * n
    visited[0] = True
    while q:
        cur = q.popleft()
        for adj in g[cur]:
            if not visited[adj]:
                dg[adj].append(cur)
                q.append(adj)
                visited[adj] = True
    for f, t in order:
        dg[t].append(f)
    visited = [False] * n
    recur = [False] * n
    def cycle(start):
        if visited[start]: return True
        if recur[start]: return False
        visited[start] = recur[start] = True
        for nxt in dg[start]:
            if cycle(nxt):
                return True
        visited[start] = False
        return False
    for i in range(n):
        if cycle(i):
            return False
    return True