n = int(input())
bstr = input()
cnt = 0
for _ in range(n-1):
    comp = list(bstr)
    cstr = list(input())
    diff = 0
    for c in cstr:
        try:
            comp.remove(c)
        except:
            diff += 1
    if diff < 2 and len(comp) < 2:
        cnt += 1    
print(cnt)