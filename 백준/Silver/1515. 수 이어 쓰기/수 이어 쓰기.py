left = input()
num, cur = 1, 0
while cur < len(left):
    snum = str(num)
    for c in snum:
        if c == left[cur]:
            cur += 1
        if cur == len(left):
            break
    num += 1
print(num - 1)