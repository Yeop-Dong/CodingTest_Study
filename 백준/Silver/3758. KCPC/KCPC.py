T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    team = [[[0] * (k+1), 0, 0] for _ in range(n+1)]
    for time in range(1, m+1):
        i, j, s = map(int, input().split())
        scores, cnt, _ = team[i]
        scores[j] = max(scores[j], s)
        team[i] = scores, cnt + 1, time
    rank = 1
    myscore, mycnt, mylast = team[t]
    myscore = sum(myscore)
    for i in range(1, n+1):
        if i == t:
            continue
        scores, cnt, last = team[i]
        scores = sum(scores)
        if scores > myscore:
            rank += 1
        elif scores == myscore:
            if mycnt > cnt:
                rank += 1
            elif mycnt == cnt and mylast > last:
                rank += 1
    print(rank)