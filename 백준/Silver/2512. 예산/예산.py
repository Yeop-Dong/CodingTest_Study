n = int(input())
req = list(map(int, input().split()))
budget = int(input())
if sum(req) <= budget:
    print(max(req))
else:
    l, r = 0, budget
    best = budget
    while l <= r:
        mid = (l + r) // 2
        sum = 0
        for q in req: 
            sum += q if q < mid else mid
            if sum > budget:
                break
        else:
            best = mid
            l = mid + 1
            continue
        r = mid - 1
    print(best)