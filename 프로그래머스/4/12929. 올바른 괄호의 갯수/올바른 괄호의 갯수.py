def solution(n):
    def sol(op, cl, st):
        if op == 0 and cl == 0 and not st:
            return 1
        l, r = 0, 0
        if op > 0:
            l = sol(op - 1, cl, st + [1])
        if cl > 0 and st:
            r = sol(op, cl - 1, st[:-1])
        return l + r
    return sol(n, n, [])