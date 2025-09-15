from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, lighthouse):
    global answer
    
    answer = 0
    v = defaultdict(list)
    for v1, v2 in lighthouse:
        v[v1].append(v2)
        v[v2].append(v1)
    record = defaultdict(bool)
    def dfs(cur, par = None):
        global answer
        for nv in v[cur]:
            if nv == par:
                continue
            dfs(nv, cur)
            if not record[nv] and not record[cur]:
                record[cur] = True
                answer += 1
    dfs(1)
    
    return answer