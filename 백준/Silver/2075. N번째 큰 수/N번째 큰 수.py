import heapq
n = int(input())
h = []
for _ in range(n):
    row = map(int, input().split())
    for num in row:
        if len(h) < n:
            heapq.heappush(h, num)
        else:
            heapq.heappushpop(h, num)
print(h[0])