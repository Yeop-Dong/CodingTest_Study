def bfs(maps, start, target):
    y, x = start
    start = (y, x, 0)
    width, height = len(maps[0]), len(maps)
    visited = [ [False for i in range(width)] for j in range(height) ]
    directions = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
    q = [start]
    visited[y][x] = True
    while q:
        y, x, depth = q.pop(0)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and visited[ny][nx] is False:
                if maps[ny][nx] == target:
                    return (ny, nx, depth+1)
                elif maps[ny][nx] != "X":
                    q.append((ny, nx, depth+1))
                    visited[ny][nx] = True
    return (-1, -1, -1)
                
def solution(maps):
    answer = 0
    start = None
    for i, row in enumerate(maps):
        for j, item in enumerate(row):
            if item == "S":
                start = (i, j)
        if start is not None:
            break
    
    lever_y, lever_x, lever_dist = bfs(maps, start, "L")
    if lever_dist == -1:
        return -1
    exit_y, exit_x, exit_dist = bfs(maps, (lever_y, lever_x), "E")
    if exit_dist == -1:
        return -1
    
    return lever_dist + exit_dist