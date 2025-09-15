import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
seq = list(map(int, input().split()))
l, r, cnt = 0, 0, 0
chk = set()
while r < n:
    if seq[r] in chk:
        while seq[r] in chk:
            chk.remove(seq[l])
            l += 1
    chk.add(seq[r])
    r += 1
    cnt += r - l
print(cnt)