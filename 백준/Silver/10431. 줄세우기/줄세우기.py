p = int(input())
for _ in range(p):
    inputs = list(map(int, input().split()))
    t, st = inputs[0], inputs[1:]
    lined = [st[0]]
    answer = 0
    for s in st[1:]:
        for i, l in enumerate(lined):
            if l > s:
                answer += len(lined) - i
                lined.insert(i, s)
                break
        else:
            lined.append(s)
    print(t, answer)
