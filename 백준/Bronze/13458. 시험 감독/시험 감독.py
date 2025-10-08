from math import ceil
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int,input().split()))
b, c = map(int, input().split())
ans = n + sum(map(lambda x: ceil((x - b) / c) if x > b else 0, a))
print(ans)
