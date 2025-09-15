import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.writelines
p, m = map(int, input().split())
room = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    for i, (state, lv, players) in enumerate(room):
        if not state and lv - 10 <= l <= lv + 10:
            players.append((l, n))
            if len(players) == m:
                state = True
            room[i] = (state, lv, players)
            break
    else:
        room.append((False if m != 1 else True, l, [(l, n)]))

for state, lv, players in room:
    print("Started!" if state else "Waiting!")
    players.sort(key = lambda x: x[1])
    for l, n in players:
        print(f"{l} {n}")