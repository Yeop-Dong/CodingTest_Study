def solution(weights):
    count = [0] * 4001
    for w in weights:
        count[w] += 1
    
    pair = 0
    for i in range(100, 1001):
        if count[i] > 0:
            pair += count[i] * (count[i] - 1) / 2
            if (i * 3 / 2 == i * 3 // 2): pair += count[i] * count[i * 3 // 2]
            pair += count[i] * count[i * 2]
            if (i * 4 / 3 == i * 4 // 3): pair += count[i] * count[i * 4 // 3]
    return pair