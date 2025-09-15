def solution(stones, k):
    n = len(stones)
    l, r = 1, max(stones)
    
    while l <= r:
        m = (l + r) // 2
        maxseqlen, seqlen = 0, 0
        satisfy = False
        for i, s in enumerate(stones):
            if s <= m:
                seqlen += 1
                if maxseqlen < seqlen:
                    maxseqlen = seqlen
                    if maxseqlen >= k:
                        satisfy = True
                        break
            else:
                seqlen = 0
            
        if satisfy:
            r = m - 1
        else:
            l = m + 1
    return l