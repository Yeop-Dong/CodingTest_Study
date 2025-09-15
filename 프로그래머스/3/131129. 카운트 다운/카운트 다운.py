def solution(target):
    DP = [ [ target, 0 ] for i in range(target + 1) ]
    DP[0][0] = 0
    for t in range(1, target + 1):
        for score in range(1, 21):
            triple = 3 * score
            if t >= triple and DP[t][0] > DP[t - triple][0]:
                DP[t] = [ DP[t - triple][0] + 1, DP[t - triple][1] ]
            double = 2 * score
            if t >= double and DP[t][0] > DP[t - double][0]:
                DP[t] = [ DP[t - double][0] + 1, DP[t - double][1] ]
            if t >= score and DP[t][0] > DP[t - score][0]:
                DP[t] = [ DP[t - score][0] + 1, DP[t - score][1] + 1 ]
        if t >= 50 and DP[t][0] > DP[t - 50][0]:
            DP[t] = [ DP[t - 50][0] + 1, DP[t - 50][1] + 1]
    return DP[target]