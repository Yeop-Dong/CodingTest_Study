def to_43200(h, m, s):
    # 360도 기준 초당 초침 6도, 분침 1/10도, 시침 1/120도
    # 43200도가 한바퀴인 각도로 변환 
    # 43200도 기준 초당 초침 720도, 분침 12도, 시침 1도
    sd = s * 720
    md = m * 720 + s * 12
    h = h if h < 12 else h - 12
    hd = h * 3600 + m * 60 + s
    
    return hd, md, sd

def next_second(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    return h, m, s

def compare_time(h1, m1, s1, h2, m2, s2):
    if h1 == h2:
        if m1 == m2:
            return s1 < s2
        return m1 < m2
    return h1 < h2

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    h, m, s = h1, m1, s1
    
    while compare_time(h, m, s, h2, m2, s2):
        nh, nm, ns = next_second(h, m, s)
        hd, md, sd = to_43200(h, m, s)
        nhd, nmd, nsd = to_43200(nh, nm, ns)
        
        nhd = nhd if nhd != 0 else 43200
        nmd = nmd if nmd != 0 else 43200
        nsd = nsd if nsd != 0 else 43200
        
        if hd >= sd and nhd < nsd:
            answer += 1
        if md >= sd and nmd < nsd:
            answer += 1
        if hd == md:
            answer -= 1
        h, m, s = nh, nm, ns
        
    if nhd == nsd or nmd == nsd:
        answer += 1
    return answer