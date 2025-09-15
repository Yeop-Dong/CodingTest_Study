directions = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]

def bfs(board, start):
    size_y, size_x = len(board), len(board[0])
    visited = [ [False for j in range(size_x)] for i in range(size_y)]
    y, x = start
    q = [ (y, x, 0) ]
    while q:
        cur = q.pop(0)
        y, x, depth = cur
        visited[y][x] = True
        if board[y][x] == 'G':
            return depth
        for dy, dx in directions:
            y, x, depth = cur
            while True:
                ny, nx = y + dy, x + dx
                if 0 <= nx < size_x and 0 <= ny < size_y and board[ny][nx] != 'D':
                    y, x = ny, nx
                else:
                    break
            if visited[y][x] == True:
                continue
            nxt = y, x, depth + 1
            q.append(nxt)  
    return -1

def solution(board):
    answer = 0
    start = None
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == "R": start = y, x
        if start is not None:
            break
    answer = bfs(board, start)
                
    return answer