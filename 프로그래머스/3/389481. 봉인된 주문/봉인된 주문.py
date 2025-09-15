def solution(n, bans):
    answer = ''
    
    def alpha_to_num(alpha):
        num = 0
        for i, a in enumerate(alpha[::-1]):
            num += 26 ** i * (ord(a) - ord('a') + 1)
        return num
    def num_to_alpha(num):
        if num == 0:
            return ''
        alpha = chr( (num - 1) % 26 + ord('a') ) 
        return num_to_alpha( (num - 1) // 26) + alpha
    bans.sort(key = lambda x: (len(x), x))
    for b in bans:
        if alpha_to_num(b) <= n:
            n += 1
    return num_to_alpha(n)