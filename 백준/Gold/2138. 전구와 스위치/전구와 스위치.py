n = int(input())
orig = input()
target = input()
orig = [o == '1' for o in orig]
target = [t == '1' for t in target]
def flip(bulb, i):
    if i > 0: bulb[i - 1] = not bulb[i - 1]
    bulb[i] = not bulb[i]
    if i < n - 1: bulb[i + 1] = not bulb[i + 1]
def chk(first = True):
    copy = orig.copy()
    cnt = 0
    if first: 
        flip(copy, 0)
        cnt += 1
    for i in range(1, n):
        if copy[i-1] != target[i-1]:
            flip(copy, i)
            cnt += 1
    if copy == target:
        return cnt
    else:
        return -1
answer = []
t = chk(True)
if t != -1: answer.append(t)
f = chk(False)
if f != -1: answer.append(f)
if len(answer) == 0: print(-1)
else: print(min(answer))