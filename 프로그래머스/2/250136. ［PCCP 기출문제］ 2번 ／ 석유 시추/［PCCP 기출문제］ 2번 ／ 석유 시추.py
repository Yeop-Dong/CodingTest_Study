def solution(land):
    n, m = len(land), len(land[0])
    pipe = [ [] for i in range(m) ]
    directions = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]

    def bfs(land, start):
        y, x = start
        connected = [x]
        quantity = 1
        q = [(y, x)]
        land[y][x] = 0
        while q:
            y, x = q.pop(0)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1:
                    q.append((ny, nx))
                    quantity += 1
                    land[ny][nx] = 0
                    if nx not in connected:
                        connected.append(nx)
        for c in connected:
            pipe[c].append(quantity)
            
    for i, row in enumerate(land):
        for j, item in enumerate(row):
            if item == 1:
                bfs(land, (i, j))
    
    return sum(max(pipe, key=sum))
        
        