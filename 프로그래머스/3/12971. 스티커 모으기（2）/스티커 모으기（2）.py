def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]
    if size == 2:
        return max(sticker)
    
    dp1 = [0] * (size - 1)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, size - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    dp2 = [0] * size
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    return max(dp1[size - 2], dp2[size - 1])
    
        
    
    
    pick2 = sticker[1] + sol(sticker, 3, len(sticker) - 1, dp)
    return pick1 if pick1 > pick2 else pick2