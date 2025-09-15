def solution(plans):
    plans.sort(key = lambda x : x[1])
    for i, p in enumerate(plans):
        name, time, duration = p
        p[1] = int(time[:2])*60 + int(time[3:])
        p[2] = int(duration)
    st = []
    finished = []
    cur = 0
    for p in plans:
        name, time, duration = p
        while st and cur + st[-1][2] <= time:
            peek = st.pop()
            finished.append(peek[0])
            cur += peek[2]
        if not st:
            st.append(p)
            cur = time
        elif cur + st[-1][2] > time:
            st[-1][2] -= time - cur
            cur = time
            st.append(p)
    while st:
        peek = st.pop()
        finished.append(peek[0])
    return finished