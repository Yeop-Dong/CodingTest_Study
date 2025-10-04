import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
gem = [ tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()
bag.sort()
hq = []
gidx = 0
result = 0
for b in bag:
    while gidx < n and gem[gidx][0] <= b:
        heapq.heappush(hq, -gem[gidx][1])
        gidx += 1
    if hq:
        result += -heapq.heappop(hq)
print(result)