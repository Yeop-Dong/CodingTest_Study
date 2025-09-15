import sys
input = lambda: sys.stdin.readline().rstrip()
chk = [[0,1,2],[3,4,5],[6,7,8], \
       [0,3,6],[1,4,7],[2,5,8], \
        [0,4,8],[2,4,6]]
def chkwin(board, side):
    for c in chk:
        if side == board[c[0]] and len(set([board[idx] for idx in c])) == 1:
            return True
    return False
results = []
while True:
    board = input()
    if board == "end":
        break
    xs, os = board.count('X'), board.count('O')
    if xs > os + 1:
        results.append(False)
        continue
    if xs == os and chkwin(board, 'O') and not chkwin(board, 'X'):
        results.append(True)
        continue
    if os > xs:
        results.append(False)
        continue
    if os + 1 == xs and chkwin(board, 'X') and not chkwin(board, 'O'):
        results.append(True)
        continue
    if xs == 5 and os == 4 and not chkwin(board, 'O'):
        results.append(True)
        continue
    results.append(False)
for r in results:
    print("valid" if r else "invalid")
