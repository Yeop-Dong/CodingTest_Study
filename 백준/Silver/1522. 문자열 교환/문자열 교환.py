s = list(input())
l = len(s)  
acnt = s.count('a')
s *= 2
best = l
for i in range(l):
    best = min(best, s[i:i+acnt].count('b'))
print(best)