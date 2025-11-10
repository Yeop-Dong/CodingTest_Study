nums =  [i * 2 for i in range(21)]
nums += [13, 16, 19]
nums += [22, 24]
nums += [28, 27, 26]
nums += [25, 30, 35]
nums += [0]
nxt = [i+1 for i in range(len(nums))]
nxt[5] = (6, 21)
nxt[23] = 29
nxt[10] = (11, 24)
nxt[15] = (16, 26)
nxt[25] = 29
nxt[20] = 32
nxt[31] = 20
GOAL = 32

faces = list(map(int, input().split()))
pieces = [0, 0, 0, 0]

def dfs(idx = 0, total = 0):
    if idx == len(faces):
        return total
    face = faces[idx]
    best = 0
    for i in range(4):
        curi = pieces[i]
        if curi == GOAL: continue
        save = curi
        steps = face
        if isinstance(nxt[curi], tuple):
            steps -= 1
            curi = nxt[curi][1]
        while steps > 0 and curi != GOAL:
            if isinstance(nxt[curi], tuple):
                curi = nxt[curi][0]
            else:
                curi = nxt[curi]
            steps -= 1
        if curi != GOAL and curi in pieces:
            continue
        pieces[i] = curi
        cand = dfs(idx+1, total + nums[curi])
        best = max(best, cand)
        pieces[i] = save
    return best

print(dfs())