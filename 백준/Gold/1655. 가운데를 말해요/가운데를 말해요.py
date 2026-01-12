import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
n = int(input())
nums = []
outs = []
for i in range(1, n+1):
    k = int(input())
    bisect.insort(nums, k)
    outs.append(nums[i//2] if i % 2 == 1 else min(nums[i//2-1], nums[i//2]))
output("\n".join(map(str, outs)))
