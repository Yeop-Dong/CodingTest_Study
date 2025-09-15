from collections import defaultdict, deque
from itertools import permutations

def solution(board, r, c):
    dirs = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
    def bfs(board, y1, x1, y2, x2):
        if (y1, x1) == (y2, x2):
            return 0
        vis = defaultdict(int)
        q = deque([(y1, x1, 0)])
        vis = [[10000] * 4 for _ in range(4)]
        vis[y1][x1] = 0
        best = 7
        while q:
            y, x, d = q.popleft()
            if d + 1 >= best:
                continue
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < 4 and 0 <= nx < 4 and d + 1 < vis[ny][nx] and d + 1 < best:
                    if (ny, nx) == (y2, x2):
                        best = min(best, d + 1)
                        continue
                    vis[ny][nx] = d + 1
                    q.append((ny, nx, d + 1))
            for dy, dx in dirs:
                for i in range(1, 5):
                    ny, nx = y + i * dy, x + i * dx
                    if 0 <= ny < 4 and 0 <= nx < 4:
                        if board[ny][nx]:
                            if d + 1 < vis[ny][nx] and d + 1 < best:
                                if (ny, nx) == (y2, x2):
                                    best = min(best, d + 1)
                                else:
                                    vis[ny][nx] = d + 1
                                    q.append((ny, nx, d + 1))
                            break
                    elif d + 1 < best:
                        if i == 1:
                            break
                        ny, nx = y + (i - 1) * dy, x + (i - 1) * dx
                        if d + 1 < vis[ny][nx]:
                            vis[ny][nx] = d + 1
                            q.append((ny, nx, d + 1))
                        break
        return best
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[board[i][j]].append((i, j))
    cardset = permutations(cards)
    best = 100000000
    b = board
    for s in cardset:
        for card in s:
            (y1, x1), (y2, x2) = cards[card]
            b[y1][x1] = b[y2][x2] = card
        y, x = r, c
        cost = len(cards) * 2
        for card in s:
            (y1, x1), (y2, x2) = cards[card]
            cand1 = bfs(b, y, x, y1, x1) + bfs(b, y1, x1, y2, x2)
            cand2 = bfs(b, y, x, y2, x2) + bfs(b, y2, x2, y1, x1)
            b[y1][x1] = b[y2][x2] = 0
            if cand1 < cand2:
                y1, x1 = y2, x2
                cand2 = cand1
            y, x = y1, x1
            cost += cand2
        best = min(best, cost)
    return best