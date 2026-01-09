from collections import deque
n, k = map(int, input().split())
tank = list(map(int, input().split()))
cnt = 0
while True:
    most, least = max(tank), min(tank)
    if most - least <= k:
        break
    tank = deque([fish] if fish != least else [fish + 1] for fish in tank)
    left = tank.popleft()
    tank[0].extend(left)
    while True:
        left = deque()
        while tank and len(tank[0]) > 1:
            left.append(tank.popleft())
        if len(left[0]) > len(tank):
            tank = left + tank
            break
        while left:
            l = left.pop()
            for top, bot in zip(l, tank):
                bot.append(top)
    tank = list(tank)
    add = [[ 0 for item in row ] for row in tank]
    for i in range(len(tank)):
        for j in range(len(tank[i])):
            if j != len(tank[i]) - 1:
                d1 = int((tank[i][j] - tank[i][j+1]) / 5)
                if d1 != 0:
                    add[i][j] -= d1
                    add[i][j+1] += d1
            if i != len(tank) - 1 and j < len(tank[i+1]):
                d2 = int((tank[i][j] - tank[i+1][j]) / 5)
                if d2 != 0:
                    add[i][j] -= d2
                    add[i+1][j] += d2
    for tanki, addi in zip(tank, add):
        for i in range(len(tanki)):
            tanki[i] += addi[i]
    tank = deque([fish] for fishes in tank for fish in fishes)
    left = deque()
    while len(left) != len(tank):
        left.append(tank.popleft())
    for tanki in tank:
        tanki.extend(left.pop())
    left = deque()
    while len(left) != len(tank):
        left.append(tank.popleft())
    for tanki in tank:
        tanki.extend(reversed(left.pop()))
    tank = list(tank)
    add = [[0] * 4 for _ in range(n // 4)]
    for i in range(n // 4):
        for j in range(4):
            if j < 3:
                d1 = int((tank[i][j] - tank[i][j+1]) / 5)
                if d1 != 0:
                    add[i][j] -= d1
                    add[i][j+1] += d1
            if i < n // 4 - 1:
                d2 = int((tank[i][j] - tank[i+1][j]) / 5)
                if d2 != 0:
                    add[i][j] -= d2
                    add[i+1][j] += d2
    tank = [tanki[i] + addi[i] for tanki, addi in zip(tank, add) for i in range(len(tanki)) ]
    cnt += 1
print(cnt)
