from collections import defaultdict
def solution(n, roads, sources, destination):
    answer = []
    adj = defaultdict(list)
    dists = defaultdict(list)
    for s, e in roads:
        adj[s].append(e)
        adj[e].append(s)
    
    def bfs(start):
        q = [start]
        depth = 0
        dists[start] = 0
        while q:
            cur = q.pop(0)
            for nxt in adj[cur]:
                if not nxt in dists:
                    q.append(nxt)
                    dists[nxt] = dists[cur] + 1
    bfs(destination)
    
    for s in sources:
        if not s in dists:
            answer.append(-1)
        else:
            answer.append(dists[s])
    return answer