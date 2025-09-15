from collections import defaultdict
n = int(input())
shortcut = defaultdict(bool)
options = []
for cnt in range(n):
    opt = input().split()
    for i, o in enumerate(opt):
        if not shortcut[o[0].lower()]:
            shortcut[o[0].lower()] = True
            options.append((opt, i, 0))
            break
    if len(options) == cnt + 1:
        continue
    for i, o in enumerate(opt):
        for k in range(1, len(o)):
            if not shortcut[o[k].lower()]:
                shortcut[o[k].lower()] = True
                options.append((opt, i, k))
                break
        if len(options) == cnt + 1:
            break
    if len(options) == cnt + 1:
        continue
    options.append((opt, None, None))
for words, widx, cidx in options:
    for i, word in enumerate(words):
        for j, c in enumerate(word):
            if i == widx and j == cidx:
                print('[' + c + ']', end='')
            else:
                print(c, end='')
        print(end = ' ')
    print()        