n = int(input())
ck = []
for _ in range(n): ck.append(input())
hy, hx = -1, -1
for i in range(n):
    for j in range(n):
        if ck[i][j] == '*':
           hy, hx = i + 1, j
           break
    if hy != -1:
        break
for j in range(hx - 1, -1, -1):
    if ck[hy][j] == '_':
        break
else:
    j = -1
larm = hx - 1 - j
for j in range(hx + 1, n):
    if ck[hy][j] == '_':
        break
else:
    j = n
rarm = j - 1 - hx
for i in range(hy + 1, n):
    if ck[i][hx] == '_':
        break
else:
    i = n
waist = i - 1 - hy
wi = i - 1
for i in range(wi + 1, n):
    if ck[i][hx - 1] == '_':
        break
else:
    i = n
lleg = i - 1 - wi
for i in range(wi + 1, n):
    if ck[i][hx+1] == '_':
        break
else:
    i = n
rleg = i - 1 - wi
print(hy + 1, hx + 1)
print(larm, rarm, waist, lleg, rleg)