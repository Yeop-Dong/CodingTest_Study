def solution(land, P, Q):
    answer = 10e99
    d1 = [0] + sum(land, [])
    ld = len(d1)
    d1.sort()
    ad1 = d1.copy()
    for i in range(1, ld):
        ad1[i] += ad1[i-1]
    i = 1
    while i < ld:
        j = i + 1
        while j < ld and d1[i] == d1[j]:
            j += 1
        lsum, rsum = ad1[i-1], ad1[-1] - ad1[j - 1]
        lest, rest = d1[i] * (i - 1), d1[i] * (ld - j)
        left, right = lest - lsum, rsum - rest
        cost = P * left + Q * right
        answer = min(answer, cost)
        i = j
    return answer