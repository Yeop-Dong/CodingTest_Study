def solution(targets):
    targets.sort()
    
    cnt = 1
    cur_s, cur_e = targets[0]
    for s, e in targets[1:]:
        if cur_s <= s < cur_e:
            cur_s = s
            if e < cur_e:
                cur_e = e
        elif cur_e <= s:
            cnt += 1
            cur_s, cur_e = s, e
    return cnt