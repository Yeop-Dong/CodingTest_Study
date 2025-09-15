def solution(n, m, x, y, queries):
    answer = -1
    rec = [x, y, x, y]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rquery = lambda cmd, dx: [dx * move[cmd][0], dx * move[cmd][1]]
    cond = ["rec[1] == 0", "rec[3] == m - 1", "rec[0] == 0", "rec[2] == n - 1"]
    chk = [1,3,0,2]
    
    make_inbound = lambda x, M: min(M - 1, max(0, x))
    for cmd, d in reversed(queries):
        dx = rquery(cmd, d) * 2
        ignore = chk[cmd] if eval(cond[cmd]) else -1
        for i, r in enumerate(rec):
            if ignore == i:
                continue
            rec[i] += dx[i]
            inbound = make_inbound(rec[i], n if i % 2 == 0 else m)
            if chk[cmd] == i and rec[i] != inbound:
                return 0
            rec[i] = inbound
    l, t, r, b = rec
    return (r - l + 1) * (b - t + 1)