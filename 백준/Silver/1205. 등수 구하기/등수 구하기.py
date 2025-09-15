n, score, p = map(int, input().split())
if n == 0:
    print("1")
else:
    nscore = list(map(int, input().split()))
    rank = 1
    for i in range(n):
        if nscore[i] > score:
            rank += 1
        if nscore[i] < score:
            break
    else:
        if n == p:
            rank = -1
    print(rank)
    