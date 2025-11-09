dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
revdir = [1, 0, 3, 2]
n, k = map(int, input().split())
board = [[2] + list(map(int, input().split())) + [2] for _ in range(n)]
board = [[2] * (n + 2)] + board + [[2] * (n+2)]
onboard = [[list() for _ in row] for row in board]
chess = [tuple(map(int, input().split())) for _ in range(k)]
chess = [(i, j, d-1) for i, j, d in chess]
for idx, (i, j, d) in enumerate(chess):
    onboard[i][j].append(idx)
game = True
turn = 0
while game and turn <= 1000:
    for idx, (i, j, d) in enumerate(chess):
        di, dj = dirs[d]
        ni, nj = i + di, j + dj
        if board[ni][nj] == 2:
            d = revdir[d]
            chess[idx] = (i, j, d)
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
        if board[ni][nj] == 2:
            continue
        fr = onboard[i][j].index(idx)
        moved = onboard[i][j][fr:]
        onboard[i][j] = onboard[i][j][:fr]
        for midx in moved:
            _, _, md = chess[midx]
            chess[midx] = (ni, nj, md)
        if board[ni][nj] == 0:
            onboard[ni][nj].extend(moved)
        elif board[ni][nj] == 1:
            onboard[ni][nj].extend(reversed(moved))
        if len(onboard[ni][nj]) >= 4:
            game = False
            break
    turn += 1
print(turn if turn <= 1000 else -1)
    