def solution(e, starts):
    answer = []
    
    DP = [ 1 for _ in range(e + 1) ]
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            DP[j] += 1
    DP2 = [ 0 for i in range(e + 1) ]
    DP2[len(DP) - 1] = len(DP) - 1
    for i in range(len(DP) - 2, -1, -1):
        DP2[i] = i if DP[i] >= DP[DP2[i+1]] else DP2[i+1]
    for s in starts:
        answer.append(DP2[s])
        
    return answer