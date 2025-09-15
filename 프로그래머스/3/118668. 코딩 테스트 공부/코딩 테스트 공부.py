def solution(alp, cop, problems):
    answer = 0
    maxa = max(problems, key=lambda x: x[0])[0]
    alp = min(alp, maxa)
    maxc = max(problems, key=lambda x: x[1])[1]
    cop = min(cop, maxc)
    DP = [ [ 1000000000 for i in range(200)] for j in range(200) ]
    DP[alp][cop] = 0
    for a in range(alp, maxa+1):
        for c in range(cop, maxc+1):
            DP[a+1][c] = min(DP[a+1][c], DP[a][c] + 1)
            DP[a][c+1] = min(DP[a][c+1], DP[a][c] + 1)
            for ar, cr, ad, cd, cost in problems:
                if a >= ar and c >= cr:
                    na = a + ad if a + ad < maxa else maxa
                    nc = c + cd if c + cd < maxc else maxc
                    DP[na][nc] = min(DP[na][nc], DP[a][c] + cost)
    return DP[maxa][maxc]