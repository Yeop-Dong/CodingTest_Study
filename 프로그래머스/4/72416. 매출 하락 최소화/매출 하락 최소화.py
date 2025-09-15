from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(sales, links):
    sales = [0] + sales
    childs = defaultdict(list)
    DP = [ [0, 0] for _ in sales ]
    for p, c in links:
        childs[p].append(c)
    def dfs(node = 1):
        childsum = 0
        gap = 2100000000
        flag = False
        for child in childs[node]:
            dfs(child)
            childsum += min(DP[child][0], DP[child][1])
            if DP[child][0] > DP[child][1]:
                flag = True
            else:
                gap = min(gap, DP[child][1] - DP[child][0])
        DP[node][1] = sales[node] + childsum
        if flag:
            DP[node][0] = childsum
        elif gap != 2100000000:
            DP[node][0] = childsum + gap
    dfs()
    return min(DP[1])