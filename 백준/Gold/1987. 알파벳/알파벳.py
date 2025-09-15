from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [False] * 26
aord = lambda c: (ord(c) - ord('A'))
visited[aord(board[0][0])] = True
def dfs(y = 0, x = 0):
    cand = []
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < r and 0 <= nx < c:
            nchr = board[ny][nx]
            if visited[aord(nchr)]: continue
            visited[aord(nchr)] = True
            cand.append(dfs(ny, nx))
            visited[aord(nchr)] = False
    return 1 + max(cand) if cand else 1
print(dfs())