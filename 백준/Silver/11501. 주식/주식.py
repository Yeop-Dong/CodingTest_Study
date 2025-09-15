import sys
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write
t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    profit, s = 0, 0
    rmax = len(stock) - 1
    for i in range(len(stock) - 2, -1, -1):
        if stock[rmax] < stock[i]:
            profit -= s
            profit += stock[rmax] * (rmax - i - 1)
            rmax = i
            s = 0
        else:
            s += stock[i]
    if rmax:
        profit -= s
        profit += stock[rmax] * rmax
    print(f"{profit}\n")