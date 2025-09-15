import sys
from collections import deque
read = lambda: sys.stdin.readline().rstrip()
write = sys.stdout.write
n = int(read())
buildings = list(map(int, read().split()))
viewl = []
viewr = deque([])
st = []
for i, b in enumerate(buildings):
    while st and st[-1][0] <= b:
        st.pop()
    viewl.append((len(st), st[-1][1] if st else -1))
    st.append((b, i))
st = []
for i, b in reversed(list(enumerate(buildings))):
    while st and st[-1][0] <= b:
        st.pop()
    viewr.appendleft((len(st), st[-1][1] if st else -1))
    st.append((b, i))
outputs = []
for i in range(n):
    lvisible, lclose = viewl[i]
    rvisible, rclose = viewr.popleft()
    visible = lvisible + rvisible
    out = str(visible) 
    if visible > 0:
        if lvisible and rvisible:
            close = rclose if i - lclose > rclose - i else lclose
        elif lvisible:
            close = lclose
        elif rvisible:
            close = rclose
        out += " " + str(close + 1)
    outputs.append(out)
write('\n'.join(outputs))
