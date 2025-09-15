def solution(money):
    answer = 0
    DP1 = [0] * len(money)
    DP2 = [0] * len(money)
    
    DP1[1] = money[1]
    DP2[0] = money[0]
    
    for i in range(2, len(money)):
        DP1[i] = max(money[i] + DP1[i-2], DP1[i-1])
    for i in range(1, len(money) - 1):
        DP2[i] = max(money[i] + DP2[i-2], DP2[i-1])
    return max(DP1[len(money) - 1], DP2[len(money) - 2])