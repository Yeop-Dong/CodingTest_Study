import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
skyline = [ tuple(map(int, input().split())) for _ in range(n) ]
skyline.sort()
cur = skyline[0][1]
st = []
cnt = 0
for s in skyline:
    flag = False
    while st and st[-1][1] > s[1]:
        flag = True
        st.pop()
    if st and st[-1][1] == s[1]:
        continue
    if s[1] == 0:
        continue
    st.append(s)
    cnt += 1
print(cnt)