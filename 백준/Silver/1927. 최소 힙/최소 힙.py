import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write
n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not hq:
            print("0\n")
            continue    
        x = heapq.heappop(hq)
        print(f"{x}\n")
        continue
    heapq.heappush(hq, x)