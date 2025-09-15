n = int(input())
row = [0] * n
info = map(int, input().split())
for i, left in enumerate(info):
    for k in range(n):
        if not row[k]:
            left -= 1
            if left < 0:
                break
    row[k] = (i+1)
for r in row:
    print(r, end=" ")
