def solution(storage, requests):
    answer = 0
    padding = [[0 for _ in range(len(storage[0]) + 2)]]
    stor = padding + [ ([0] + [item for item in row] + [0]) for row in storage ] + padding
    directions = [ (-1, 0), (1, 0), (0, 1), (0, -1)]
    def bfs(start, target):
        cnt = 0
        req = len(target)
        if req == 2:
            target = target[0]
            for i, row in enumerate(stor):
                for j, item in enumerate(row):
                    if item == target:
                        stor[i][j] = 0
                        cnt += 1
            return cnt
        
        visited = [ [False for j in row ] for row in stor ]
        q = [start]
        y, x = start
        visited[y][x] = True
        while q:
            y, x = q.pop(0)
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(stor) and 0 <= nx < len(stor[0]) and not visited[ny][nx]:
                    if stor[ny][nx] == 0:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                    elif stor[ny][nx] == target:
                        stor[ny][nx] = 0
                        cnt += 1
                        visited[ny][nx] = True
                        
        return cnt
    
    for r in requests:
        answer += bfs((0, 0), r)
        
    return len(storage[0]) * len(storage) - answer