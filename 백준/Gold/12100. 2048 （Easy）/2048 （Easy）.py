from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
def left(board):
    nboard = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp = deque([x for x in board[i] if x != 0])
        k = 0
        while tmp:
            sv = tmp.popleft()
            if not tmp:
                nboard[i][k] = sv
                break
            nxt = tmp.popleft()
            if sv == nxt:
                nboard[i][k] = 2 * sv
            else:
                nboard[i][k] = sv
                tmp.appendleft(nxt)
            k += 1
    return nboard
def right(board):
    nboard = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp = deque([x for x in board[i] if x != 0])
        k = n - 1
        while tmp:
            sv = tmp.pop()
            if not tmp:
                nboard[i][k] = sv
                break
            nxt = tmp.pop()
            if sv == nxt:
                nboard[i][k] = 2 * sv
            else:
                nboard[i][k] = sv
                tmp.append(nxt)
            k -= 1
    return nboard
def up(board):
    nboard = [[0] * n for _ in range(n)]
    for j in range(n):
        tmp = deque([board[i][j] for i in range(n) if board[i][j] != 0])
        k = 0
        while tmp:
            sv = tmp.popleft()
            if not tmp:
                nboard[k][j] = sv
                break
            nxt = tmp.popleft()
            if sv == nxt:
                nboard[k][j] = 2 * sv
            else:
                nboard[k][j] = sv
                tmp.appendleft(nxt)
            k += 1
    return nboard
def down(board):
    nboard = [[0] * n for _ in range(n)]
    for j in range(n):
        tmp = deque([board[i][j] for i in range(n) if board[i][j] != 0])
        k = n - 1
        while tmp:
            sv = tmp.pop()
            if not tmp:
                nboard[k][j] = sv
                break
            nxt = tmp.pop()
            if sv == nxt:
                nboard[k][j] = 2 * sv
            else:
                nboard[k][j] = sv
                tmp.append(nxt)
            k -= 1
    return nboard
funcs = [up, down, left, right]
def bruteforce(board, dep = 0):
    if dep == 5:
        return max(map(max, board))
    ans = 0
    for fx in funcs:
        nboard = fx(board)
        ans = max(ans, bruteforce(nboard, dep + 1))
    return ans
print(bruteforce(board))