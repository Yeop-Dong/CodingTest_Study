n = int(input())
bodies = []
for _ in range(n):
    bodies.append(tuple(map(int, input().split())))
for w, h in bodies:
    rank = 1
    for iw, ih in bodies:
        if iw > w and ih > h:
            rank += 1
    print(rank, end = " ")
