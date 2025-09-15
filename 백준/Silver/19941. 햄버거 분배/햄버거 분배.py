n, k = map(int, input().split())
ph = [i for i in input()]
cnt = 0
for i in range(n):
    if ph[i] == 'P':
        left = max(0, i - k)
        right = min(n, i + k + 1)
        for h in range(left, right):
            if ph[h] == 'H':
                ph[h] = 'X'
                cnt += 1
                break
print(cnt)