def solution(n, tops):
    DP = [[0, 0] for i in range(n+1)]
    DP[1] = [4, 3] if tops[0] == 1 else [3, 2]
    for i in range(2, n+1):
        s, o = DP[i-1][0], DP[i-1][1]
        DP[i] = [s*3+o, s*2+o] if tops[i-1] == 1 else [s*2+o, s + o]
        DP[i] = [DP[i][0] % 10007, DP[i][1] % 10007]
    return DP[n][0]