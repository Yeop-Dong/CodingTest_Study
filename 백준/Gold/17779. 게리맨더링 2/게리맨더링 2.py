import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
grid = [ list(map(int, input().split())) for _ in range(n)]
def calc(x, y, d1, d2):
    tmp = [[-1] * n for _ in range(n)]
    for i in range(d1+1):
        tmp[x+i][y-i] = 5
        tmp[x+d2+i][y+d2-i]=5
    for i in range(d2+1):
        tmp[x+i][y+i] = 5
        tmp[x+d1+i][y-d1+i] = 5
    for i in range(x+1, x+d1+d2):
        fill = False
        for j in range(n):
            if tmp[i][j] == 5:
                fill = not fill
            if fill:
                tmp[i][j] = 5
    for i in range(x + d1):
        for j in range(y + 1):
            if tmp[i][j] == 5: break
            tmp[i][j] = 1
    for i in range(x + d2 + 1):
        for j in range(n - 1, y, -1):
            if tmp[i][j] == 5: break
            tmp[i][j] = 2
    for i in range(x + d1, n):
        for j in range(y-d1+d2):
            if tmp[i][j] == 5: break
            tmp[i][j] = 3
    for i in range(x + d2 + 1, n):
        for j in range(n - 1, y - d1 + d2 - 1, -1):
            if tmp[i][j] == 5: break
            tmp[i][j] = 4
    pop = [0] * 5
    for i in range(n):
        for j in range(n):
            pop[tmp[i][j] - 1] += grid[i][j]
    return max(pop) - min(pop)

mindiff = float('inf')
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x + d1 + d2 >= n: continue
                if y - d1 < 0 or y + d2 >= n: continue
                mindiff = min(mindiff, calc(x, y, d1, d2))
print(mindiff)