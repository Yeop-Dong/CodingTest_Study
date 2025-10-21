rtip, ltip = 2, 6
wh = [list(map(int, input())) for _ in range(4)]
k = int(input())
cmd = [ tuple(map(int, input().split())) for _ in range(k) ]
cmd = [ (w - 1, t) for w, t in cmd]
state = [0] * 4
idx = lambda w, i: (8 * k + state[w] + i) % 8
def rotate(w, t):
    willrotate = [0] * 4
    willrotate[w] = t
    for l in range(w, 0, -1):
        if wh[l][idx(l, ltip)] == wh[l-1][idx(l - 1, rtip)]:
            break
        willrotate[l - 1] = -willrotate[l]
    for r in range(w, 3):
        if wh[r][idx(r, rtip)] == wh[r+1][idx(r + 1, ltip)]:
            break
        willrotate[r + 1] = -willrotate[r]
    for i in range(4):
        state[i] -= willrotate[i]
for w, t in cmd:
    rotate(w, t)
score = 0
for i in range(4):
    if wh[i][idx(i, 0)] == 1:
        score += 2 ** i
print(score)