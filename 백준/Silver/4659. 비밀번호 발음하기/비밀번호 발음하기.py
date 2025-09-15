while True:
    pw = input()
    if pw == "end":
        break
    vow = "aeiou"
    acceptable = True
    if not any([v in pw for v in vow]):
        acceptable = False
    conv, conc = 0, 0
    if acceptable:
        for p in pw:
            if p in vow:
                conc = 0
                conv += 1
            else:
                conc += 1
                conv = 0
            if conc >= 3 or conv >= 3:
                acceptable = False
                break
    if acceptable:
        for i in range(len(pw) - 1):
            if pw[i] == pw[i + 1]:
                if pw[i] == "e" or pw[i] == "o":
                    continue
                acceptable = False
                break
    msg = f"<{pw}> is {'' if acceptable else 'not '}acceptable."
    print(msg)
