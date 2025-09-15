from collections import defaultdict
def solution(board):
    answer = 0
    n = len(board)
    blk = defaultdict(set)
    rec = defaultdict(tuple)
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item:
                blk[item].add((i, j))
    for b in blk:
        miny, minx, maxy, maxx = 201,201,-1,-1
        for y, x in blk[b]:
            miny, minx = min(miny, y), min(minx, x)
            maxy, maxx = max(maxy, y), max(maxx, x)
        rec[b] = ((miny, minx), (maxy, maxx))
    while blk:
        able = []
        for b in blk:
            cnt = 0
            (miny, minx), (maxy, maxx) = rec[b]
            for i in range(miny, maxy+1):
                for j in range(minx, maxx+1): 
                    if (i, j) not in blk[b]:
                        for m in range(i, -1, -1):
                            if board[m][j]:
                                break
                        else:
                            cnt += 1
            if cnt == 2:
                able.append(b)
        if not able:
            break
        for a in able:
            answer += 1
            for i, j in blk[a]:
                board[i][j] = 0
            del blk[a]
    
    return answer