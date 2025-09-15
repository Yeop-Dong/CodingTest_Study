def solution(diffs, times, limit):
    tsum = [0] + [ times[i] + times[i-1] for i in range(1, len(times)) ]
    l = 1
    r = max(diffs)
    cnt = 0
    while r >= l:
        cnt += 1
        time = 0
        m = (l + r) // 2
        for i, d in enumerate(diffs):
            if d > m:
                time += tsum[i] * (d - m) + times[i]
            else:
                time += times[i]
        if time <= limit:
            r = m - 1
        else:
            l = m + 1
    return l