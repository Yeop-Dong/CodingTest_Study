def solution(words):
    t = {"root": (0, {})}
    
    for word in words:
        v, c = t["root"]
        for ch in word:
            if c.get(ch, None):
                nv, nc = c[ch]
                c[ch] = (nv + 1, nc)
                c = nc
            else:
                c[ch] = (1, {})
                c = c[ch][1]
    answer = 0
    for word in words:
        v, c = t["root"]
        for ch in word:
            v, c = c[ch]
            answer += 1
            if v == 1:
                break
    return answer