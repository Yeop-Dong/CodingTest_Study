N, K = map(int, input().split())
nations = [0 for _ in range(N)]
for _ in range(N):
    nation, g, e, d = map(int, input().split())
    nations[nation - 1] = (g, e, d)
K -= 1
kg, ke, kd = nations[K]
result = 1
for g, e, d in nations:
    if g > kg:
        result += 1
        continue
    elif g == kg:
        if e > ke:
            result += 1
            continue
        elif e == ke and d > kd:
            result += 1
            continue
print(result)