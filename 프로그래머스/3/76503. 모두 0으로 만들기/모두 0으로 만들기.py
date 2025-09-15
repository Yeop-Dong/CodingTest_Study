from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(a, edges):
    answer = 0
    adj = defaultdict(list)
    if sum(a) != 0:
        return -1
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    def dfs(cur, parent):
        acc = 0
        for op in adj[cur]:
            if op == parent:
                continue
            acc += dfs(op, cur)
        result = abs(a[cur])
        if parent == -1:
            if result != 0:
                return -1
            else:
                return acc
        a[parent] += a[cur]
        a[cur] = 0
        return acc + result
    
    answer = dfs(0, -1)
    
    return answer
    
    