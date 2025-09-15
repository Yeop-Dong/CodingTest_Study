import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write
n = int(input())
arr = list(map(int, input().split()))
st = []
result = []
for i, a in enumerate(arr):
    while st:
        peek = st[-1]
        if peek[0] >= a:
            break
        st.pop()
    if st:
        result.append(st[-1][1] + 1)
    else:
        result.append(0)
    st.append((a, i))
print(' '.join([str(r) for r in result]))