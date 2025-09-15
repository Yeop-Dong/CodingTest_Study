from queue import PriorityQueue
def solution(land, height):
    answer = 0
    n = len(land)
    q = PriorityQueue()
    parents = [ [ 0 ] * n for _ in range(n) ]
    
    def find(y, x):
        if parents[y][x] == (y, x):
            return y, x
        ny, nx = parents[y][x]
        parents[y][x] = find(ny, nx)
        return parents[y][x]
    def union(y1, x1, y2, x2):
        y1, x1 = find(y1, x1)
        y2, x2 = find(y2, x2)
        if (y1, x1) == (y2, x2):
            return False
        
        if (y1, x1) < (y2, x2):
            parents[y2][x2] = y1, x1
        else:
            parents[y1][x1] = y2, x2
        return True
            
    delta = [ (0, 1), (1, 0) ]
    for y in range(n):
        for x in range(n):
            parents[y][x] = (y, x)
            for dy, dx in delta:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n:
                    diff = abs(land[y][x] - land[ny][nx])
                    diff = diff if diff > height else 0
                    q.put((diff, (y, x, ny, nx)))
    
    while not q.empty():
        diff, (y, x, ny, nx) = q.get()
        if union(y, x, ny, nx):
            answer += diff
        
    
    return answer