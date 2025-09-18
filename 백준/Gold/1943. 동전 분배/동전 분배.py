import sys
from collections import defaultdict
input = lambda: sys.stdin.readline()
output = sys.stdout.write
def chk():
    n = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(n)]
    total = sum(map(lambda coin: coin[0] * coin[1], coins))
    if total % 2 == 1:
        return False
    total //= 2
    dp = defaultdict(bool)
    dp[0] = True
    for coin, cnt in coins:
        for money in list(dp.keys()):
            if dp[money]:
                for i in range(1, cnt+1):
                    dp[money+coin*i] = True
    return dp[total]
outs = ''
for _ in range(3):
    outs += '1\n' if chk() else '0\n'
output(outs)