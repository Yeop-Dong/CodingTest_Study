def solution(picks, minerals):
    if len(minerals) < 0 or sum(picks) == 0:
        return 0
    fatigue = [ {"diamond": 1, "iron": 1, "stone": 1},
               {"diamond": 5, "iron": 1, "stone": 1},
               {"diamond": 25, "iron": 5, "stone": 1}]
    
    fats = []
    for i, p in enumerate(picks):
        if p == 0:
            continue
        nxt = picks[:]
        nxt[i] -= 1
        end = min(5, len(minerals))
        f = 0
        for t in range(end):
            f += fatigue[i][minerals[t]]
        f += solution(nxt, minerals[end:])
        fats.append(f)
    return min(fats)