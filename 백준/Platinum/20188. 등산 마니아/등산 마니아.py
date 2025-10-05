import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
con = [[] for _ in range(n+1)]
global ans
ans = 0
for i in range(n - 1):
    a, b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)
def dfs(v: int, p: int):
    global ans
    cnt = 1
    for nv in con[v]:
        if p == nv: continue
        sub = dfs(nv, v)
        ans += sub * (n - sub) + sub * (sub - 1) // 2
        cnt += sub
    return cnt
dfs(1, 1)
print(ans)
