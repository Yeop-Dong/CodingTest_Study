from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)
def solution(info, edges):
    vout = defaultdict(list)
    for s, e in edges:
        vout[s].append(e)
    vinfo = [ 0 for _ in info ]
    best = [0, 0]
    def full(v, nxts, sheep, wolf):
        if info[v] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if sheep <= wolf:
            return
        
        if sheep > best[0]:
            best[0] = sheep
            best[1] = wolf
            
        next_nxts = nxts + vout[v]
        for nv in next_nxts:
            full(nv, [nxt for nxt in next_nxts if nxt != nv], sheep, wolf)
        

    full(0, [], 0, 0)
    return best[0]     