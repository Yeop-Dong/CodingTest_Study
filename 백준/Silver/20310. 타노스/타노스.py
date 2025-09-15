s = input()
c1, c0 = 0, 0
for c in s:
    if c == '1': c1 += 1
    else: c0 += 1
c1 //= 2
c0 //= 2
dels = []
for i in range(len(s)):
    if s[i] == '1': 
        dels.append(i)
        c1 -= 1
        if c1 == 0:
            break
for i in range(len(s) - 1, -1, -1):
    if s[i] == '0':
        dels.append(i)
        c0 -= 1
        if c0 == 0:
            break
s = ''.join([c for i, c in enumerate(s) if i not in dels])
print(s)