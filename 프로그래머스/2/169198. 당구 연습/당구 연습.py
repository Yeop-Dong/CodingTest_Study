import math
def calc(x1, y1, x2, y2):
    return math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        dists = []
        if not (startX == x and startY < y):
            dists.append(calc(x, y, startX, 2 * n -startY))
        if not (startX == x and startY > y):
            dists.append(calc(x, y, startX, -startY))
        if not (startY == y and startX < x):
            dists.append(calc(x, y, 2 * m - startX, startY))
        if not (startY == y and startX > x):
            dists.append(calc(x, y, -startX, startY))
        
        answer.append(min(dists))
    return answer