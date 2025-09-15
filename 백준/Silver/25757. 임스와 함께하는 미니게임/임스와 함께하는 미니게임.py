games = { "Y": 2, "F": 3, "O": 4 }
n, game = input().split()
n, game = int(n), games[game] - 1
player = set()
for _ in range(n):
    player.add(input())
print(len(player) // game)