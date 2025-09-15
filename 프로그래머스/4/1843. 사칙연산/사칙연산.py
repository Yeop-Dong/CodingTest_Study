def solution(arr):
    # - 나오는 이후 값 최소로, 최소로 만들수 없으면 - 먼저
    n = len(arr) // 2 + 1
    INF = 2100000000
    M, m = [[-INF] * n for _ in range(n)], [[INF] * n for _ in range(n)]
    operator, operand = lambda i: arr[2*i+1], lambda i: int(arr[2*i])
    
    for k in range(n):
        for s in range(n - k):
            if k == 0:
                M[s][s] = m[s][s] = operand(s)
                continue
            e = s + k
            for b in range(s, e):
                op = operator(b)
                if op == '+':
                    M[s][e] = max(M[s][e], M[s][b] + M[b+1][e])
                    m[s][e] = min(m[s][e], m[s][b] + m[b+1][e])
                else:
                    M[s][e] = max(M[s][e], M[s][b] - m[b+1][e])
                    m[s][e] = min(m[s][e], m[s][b] - M[b+1][e])
    return M[0][-1]
                
    