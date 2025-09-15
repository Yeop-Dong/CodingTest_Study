n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]
total, m = 0, price[0]
for i in range(n - 1):
    m = min(m, price[i])
    total += m * dist[i]
print(total)