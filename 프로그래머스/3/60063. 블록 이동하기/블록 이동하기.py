from collections import defaultdict
def solution(board):
    answer = 0
    cur = [(0, 0), (0, 1), "h"]
    moves = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]
    N = len(board) - 1
    # rotate["현재 방향"] = [ (이동하는 부분, 이동량, 이동하는 부분 기준 체크할 상대위치) ]
    rotates = { 
        "h": [ 
            (0, (1, 1), (1, 0)),
            (1, (1, -1), (1, 0)),
            (0, (-1, 1), (-1, 0)),
            (1, (-1, -1), (-1, 0))
        ],
        "v": [
            (0, (1, 1), (0, 1)),
            (0, (1, -1), (0, -1)),
            (1, (-1, -1), (0, -1)),
            (1, (-1, 1), (0, 1))
        ]
    }
    def boundarychk(x):
        return 0 <= x <= N
    def valuechk(r, c):
        return board[r][c] == 0
    def bfs():
        visited = defaultdict(bool)
        q = [ (cur, 0) ]
        visited[(0, 0, 0, 1)] = True
        while q:
            ((r1, c1), (r2, c2), state), depth = q.pop(0)
            for dy, dx in moves:
                nr1, nc1 = r1 + dy, c1 + dx
                nr2, nc2 = r2 + dy, c2 + dx
                nr1, nc1 = min((nr1, nc1), (nr2, nc2))
                nr2, nc2 = max((nr1, nc1), (nr2, nc2))
                bchk = all(boundarychk(x) for x in [nr1, nc1, nr2, nc2])
                if bchk and not visited[(nr1, nc1, nr2, nc2)]:
                    if all(valuechk(r, c) for r, c in [(nr1, nc1), (nr2, nc2) ]):
                        if (nr1, nc1) == (N, N) or (nr2, nc2) == (N, N):
                            return depth + 1
                        q.append( ( ((nr1, nc1), (nr2, nc2), state), depth + 1 ) )
                        visited[(nr1, nc1, nr2, nc2)] = True
            for change, (dy, dx), (chkdy, chkdx) in rotates[state]:
                r, c = r1, c1
                leftr, leftc = r2, c2
                if change == 1:
                    r, c = r2, c2
                    leftr, leftc = r1, c1
                chkr, chkc = r + chkdy, c + chkdx
                if any(not boundarychk(x) for x in [chkr, chkc]):
                    continue
                if not valuechk(chkr, chkc):
                    continue
                nr, nc = r + dy, c + dx
                nr1, nc1 = min((nr, nc), (leftr, leftc))
                nr2, nc2 = max((nr, nc), (leftr, leftc))
                nstate = "h" if state == "v" else "v"
                bchk = all(boundarychk(x) for x in [nr1, nc1, nr2, nc2])
                if bchk and not visited[(nr1, nc1, nr2, nc2)]:
                    if all(valuechk(r, c) for r, c in [(nr1, nc1), (nr2, nc2) ]):
                        if (nr1, nc1) == (N, N) or (nr2, nc2) == (N, N):
                            return depth + 1
                        q.append( ( ((nr1, nc1), (nr2, nc2), nstate), depth + 1 ) )
                        visited[(nr1, nc1, nr2, nc2)] = True
            
    answer = bfs()
    return answer