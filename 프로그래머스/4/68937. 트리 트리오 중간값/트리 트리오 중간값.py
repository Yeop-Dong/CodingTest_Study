from collections import defaultdict
def solution(n, edges):
    answer = 0
    g = defaultdict(list)
    for v1, v2 in edges:
        g[v1].append(v2)
        g[v2].append(v1)
    def bfs(start):
        visited = defaultdict(bool)
        q = []
        q.append([start])
        visited[start] = True
        while q[-1]:
            q.append([])
            for cur in q[-2]:
                for nxt in g[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q[-1].append(nxt)
        return q[-2], len(q) - 2
    
    l1, d1 = bfs(1)
    l2, d2 = bfs(l1[0])
    if len(l1) == 1 and len(l2) == 1:
        return d2 - 1
    else:
        l3, d3 = bfs(l2[0])
        return d3