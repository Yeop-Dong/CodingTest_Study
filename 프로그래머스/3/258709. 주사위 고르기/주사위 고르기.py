from itertools import combinations
def solution(dice):
    n = len(dice)
    wins = []
    def outcomecnt(mask):
        maxsum = 0
        for i in range(n):
            if mask & (1 << i) == 0: continue
            maxsum += dice[i][-1]
        DP = [ 0 for _ in range(maxsum + 1) ]
        DP[0] = 1
        for i in range(n):
            if mask & (1 << i) == 0: continue
            NDP = [ 0 for _ in range(maxsum + 1) ]
            for cnt in range(maxsum+1):
                if DP[cnt] == 0: continue
                for d in dice[i]:
                    NDP[cnt + d] += DP[cnt]
            DP = NDP
        return DP
        
    def countwins(maskA):
        fullmask = (1 << n) - 1
        maskB = ~maskA & fullmask
        outcomeA = outcomecnt(maskA)
        outcomeB = outcomecnt(maskB)
        for i in range(1, len(outcomeB)):
            outcomeB[i] += outcomeB[i-1]
        win = 0
        for i in range(2, len(outcomeA)):
            BunderA = outcomeB[min(i - 1, len(outcomeB) - 1)]
            win += BunderA * outcomeA[i]
        return win
        
    dice = list(map(sorted, dice))
    maxwin, maxmask = 0, 0
    for i in range(0, 1 << n):
        if bin(i).count('1') != n // 2: continue
        win = countwins(i)
        if maxwin < win:
            maxwin = win
            maxmask = i
    for i, m in enumerate(reversed(bin(maxmask))):
        if m == 'b': break
        if m == '0': continue
        wins.append(i + 1)
    return wins