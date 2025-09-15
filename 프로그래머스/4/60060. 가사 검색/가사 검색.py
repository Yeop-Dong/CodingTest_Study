def solution(words, queries):
    answer = []
    
    def add(tree, ch, l):
        if tree.get((ch, l), None) is None:
            tree[(ch, l)] = (1, {})
            return tree[(ch, l)][1]
        nl, nd = tree[(ch, l)]
        tree[(ch, l)] = (nl + 1, nd)
        return nd
    
    t, rt = {}, {}
    for word in words:
        c = t
        n = len(word)
        for ch in word:
            c = add(c, ch, n)
        c = rt
        for ch in word[::-1]:
            c = add(c, ch, n)
    for query in queries:
        q, c = (query, t) if query.endswith('?') else (query[::-1], rt)
        
        n = len(q)
        size = 0
        if q[0] == '?':
            for ch, l in c:
                if l == n:
                    size += c[ch, l][0]
        else:
            for ch in q:
                if ch == '?' or c == None: break
                size, c = c.get((ch, n), (0, None))
        answer.append(size)
        
    return answer