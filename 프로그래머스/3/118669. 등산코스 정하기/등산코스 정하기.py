from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    v = defaultdict(list)
    for i, j, w in paths:
        v[i].append((j, w))
        v[j].append((i, w))
    dp = [10000001] * (n+1)
    gchk = [False] * (n+1)
    schk = [False] * (n+1)
    for g in gates:
        gchk[g] = True
    for s in summits:
        schk[s] = True
    def dijk(start):
        dist = [10000001] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        while q:
            intensity, v1 = heapq.heappop(q)
            if schk[v1]:
                break
            if dist[v1] < intensity:
                continue
            for v2, w in v[v1]:
                if gchk[v2]:
                    continue
                nintensity = max(intensity, w)
                if dist[v2] > nintensity:
                    dist[v2] = nintensity
                    dp[v2] = min(dp[v2], nintensity)
                    heapq.heappush(q, (nintensity, v2))

    for g in gates:
        dijk(g)
    minK, minV = -1, 10000001
    for s in summits:
        if dp[s] < minV:
            minV = dp[s]
            minK = s
        elif dp[s] == minV and minK > s:
            minK = s
    return [minK, minV]