def R(a):
    r = [[0] * 100 for _ in range(len(a))]
    maxlen = 0
    for i in range(len(a)):
        cnts = {}
        for j in range(len(a[0])):
            if a[i][j]:
                cnts[a[i][j]] = cnts.get(a[i][j], 0) + 1
        tmp = sorted(list(cnts.items()), key=lambda x: (x[1], x[0]))
        for j in range(min(len(tmp), 50)):
            r[i][2*j] = tmp[j][0]
            r[i][2*j+1] = tmp[j][1]
        maxlen = max(maxlen, len(tmp) * 2)
    maxlen = min(maxlen, 100)
    return [row[:maxlen] for row in r]

def C(a):
    trans = list(zip(*a))
    rtrans = R(trans)
    return list(map(list, zip(*rtrans)))
r, c, k = map(int, input().split())
r, c = r - 1, c - 1
a = [list(map(int, input().split())) for _ in range(3)]
for t in range(101):
    if r < len(a) and c < len(a[0]) and a[r][c] == k:
        print(t)
        break
    if len(a) >= len(a[0]):
        a = R(a)
    else:
        a = C(a)
else:
    print("-1")