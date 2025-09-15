input()
s = [-1] + list(map(int, input().split()))
n = int(input())
for _ in range(n):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, len(s), num):
            s[i] = 0 if s[i] else 1
    if sex == 2:
        l, r = num - 1, num + 1
        s[num] = 0 if s[num] else 1
        while l >= 1 and r < len(s) and s[l] == s[r]:
            s[l] = 0 if s[l] else 1
            s[r] = 0 if s[r] else 1
            l -= 1
            r += 1

for i in range(1, len(s)):
    end = " "
    if i % 20 == 0:
        end = "\n"
    print(s[i], end = end)