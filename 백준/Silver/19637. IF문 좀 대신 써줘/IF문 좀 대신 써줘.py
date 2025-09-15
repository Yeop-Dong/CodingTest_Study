import bisect
import sys
input = lambda : sys.stdin.readline().rstrip()
print = lambda x: sys.stdout.write(x)
n, m = map(int, input().split())
honor = []
for _ in range(n):
    title, ubound = input().split()
    honor.append((title, int(ubound)))
output = []
for _ in range(m):
    power = int(input())
    title, _ = honor[bisect.bisect_left(honor, power, key=lambda x: x[1])]
    output.append(title)
print('\n'.join(output))