n, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def check(line):
    slope = [False] * n
    for i in range(n - 1):
        if line[i] == line[i+1]: continue
        if abs(line[i] - line[i+1]) > 1: return False
        if line[i] < line[i+1]:
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != line[i] or slope[j]:
                    return False
                slope[j] = True
        else:
            for j in range(i + 1, i + l + 1):
                if j >= n or line[j] != line[i+1] or slope[j]:
                    return False
                slope[j] = True
    return True

cnt = 0
for g in grid:
    if check(g): 
        cnt += 1
for j in range(n):
    if check([grid[i][j] for i in range(n)]):
        cnt += 1
print(cnt)